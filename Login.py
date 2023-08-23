from pydantic import BaseModel
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from helper import get_db , verify_password
from jose import jwt
from datetime import datetime, timedelta


class UserCreate(BaseModel):
    username: str
    password: str


loginRouter = APIRouter()


@loginRouter.post("/login", response_model=str)
def login_access_token(user: UserCreate, db: Session = Depends(get_db)):
    username = user.username
    password = user.password
    
    # Retrieve user from the database
    db_user = db.query(User).filter(User.name == username).first()
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token_data = {
        "sub": str(db_user.id),  
        "exp": datetime.utcnow() + timedelta(days=1)  
    }
    secret_key = b'3v5w9z$C&F)J@NcRfUjXn2r5u7x!A%D*'

    token = jwt.encode({"id": str(db_user.id)}, secret_key, algorithm='HS256')
    return token
