from fastapi import FastAPI , Request
from models import engine , Base 
from Signup import router 
from Login import loginRouter
from protected_get_1 import protectedRoute
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# Create FastAPI app instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/Login")
def index(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})

@app.get("/Signup")
def index(request: Request):
    return templates.TemplateResponse("Singup.html", {"request": request})

app.include_router(router)
app.include_router(loginRouter)
app.include_router(protectedRoute)