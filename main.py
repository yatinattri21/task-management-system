from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
from auth import get_current_user, create_access_token, authenticate_user, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

@app.post("/register", response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(400, "User already exists")
    new_user = crud.create_user(db, user.username, user.password)
    token = create_access_token({"sub": new_user.username})
    return {"access_token": token}

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(401, "Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token}

@app.get("/tasks", response_model=list[schemas.TaskOut])
def list_tasks(skip: int = 0, limit: int = 10, status: str = None,
               db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.get_tasks(db, user.id, skip, limit, status)

@app.post("/tasks", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_task(db, task, user.id)

@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = crud.get_task(db, task_id, user.id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.update_task(db, task_id, user.id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    crud.delete_task(db, task_id, user.id)
    return {"detail": "Deleted"}