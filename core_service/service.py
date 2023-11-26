import os
import logging
from fastapi import APIRouter, Depends, HTTPException
from config.database import SessionLocal, engine
from .models import Base

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


log_filename = "logger/qaModule.log"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
logging.basicConfig(filename='logger/qaService.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


core_service = APIRouter()