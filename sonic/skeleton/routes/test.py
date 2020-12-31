from fastapi import APIRouter, Depends, HTTPException, Header
from typing import Optional
import schemas

router = APIRouter()

@router.get('/', response_model = str) 
def test():
    return "Hello world 🤩"