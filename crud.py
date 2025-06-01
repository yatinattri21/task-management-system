from sqlalchemy.orm import Session
from models import Task, User
from schemas import TaskCreate, TaskUpdate
from utils import get_password_hash

def create_user(db: Session, username: str, password: str):
    hashed = get_password_hash(password)
    user = User(username=username, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 10, status: str = None):
    query = db.query(Task).filter(Task.owner_id == user_id)
    if status:
        query = query.filter(Task.status == status)
    return query.offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, user_id: int, task: TaskUpdate):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        for k, v in task.dict(exclude_unset=True).items():
            setattr(db_task, k, v)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        db.delete(db_task)
        db.commit()