from pydantic import BaseModel
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from helper import get_password_hash, get_db
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

class UserCreate(BaseModel):
    username: str
    password: str


router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.name == user.username).first():
        raise HTTPException(
            status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user.password)

    new_user = User(name=user.username, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token_data = {
        "sub": str(new_user.id), 
        "exp": datetime.utcnow() + timedelta(days=1),  
        "audience": "my-fastapi-app"
    }
    secret_key = os.getenv("SECRETKEY")

    token = jwt.encode(token_data, secret_key, algorithm='HS256')
    print(token)

    return {"ok": True, "message": "User created successfully", "token": token}
