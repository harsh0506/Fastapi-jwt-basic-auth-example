from pydantic import BaseModel
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from models import User
from helper import get_password_hash, get_db
from jose import jwt
from datetime import datetime, timedelta


class UserCreate(BaseModel):
    username: str
    password: str


router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username is already taken
    if db.query(User).filter(User.name == user.username).first():
        raise HTTPException(
            status_code=400, detail="Username already registered")

    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Create a new User instance
    new_user = User(name=user.username, hashed_password=hashed_password)

    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Generate a JWT token
    token_data = {
        "sub": str(new_user.id),  # subject: user's ID
        "exp": datetime.utcnow() + timedelta(days=1),  # token expiration time
        "audience": "my-fastapi-app"
    }
    secret_key = "resoluteai-secretkey"  # Replace with your secret key

    token = jwt.encode(token_data, secret_key, algorithm='HS256')
    print(token)

    return {"ok": True, "message": "User created successfully", "token": token}
