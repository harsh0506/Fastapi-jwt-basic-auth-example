from fastapi import HTTPException, APIRouter
from jose import jwt ,ExpiredSignatureError, JWTError
from pydantic import BaseModel
protectedRoute = APIRouter()

SECRET_KEY = b'3v5w9z$C&F)J@NcRfUjXn2r5u7x!A%D*'

class Token(BaseModel):
    token: str

def verify_token(token: str) -> str:
    try:
        print(token)
        
        return "Token is valid"
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token validation failed")

@protectedRoute.post("/protected")
def protected_route(token_body: Token):
    print(token_body.token)
    payload = jwt.decode(token_body.token, SECRET_KEY, algorithms=["HS256"])
    print(payload)
    return {"message": "Token is valid"}
    





