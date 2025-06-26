from fastapi import APIRouter, Form, HTTPException
from config import username, password

router = APIRouter()

@router.post("/api/login")
def login(username_input: str = Form(...), password_input: str = Form(...)):
    if username_input == username and password_input == password:
        return {"message": "ok", "user": username_input}
    raise HTTPException(status_code=401, detail="Invalid credentials")
