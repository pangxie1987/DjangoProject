from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import curd, models, schemas
from .databases import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_bd():
	'获取数据库'
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()