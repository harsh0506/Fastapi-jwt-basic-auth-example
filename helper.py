from passlib.context import CryptContext
from models import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return pwd_context.verify(password, hashed_pass)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()