from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# from . import curd, models, schemas
import curd, models, schemas
from databases import SessionLocal, engine
from starlette.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_bd():
	'获取数据库'
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()

@app.post("/comment/", response_model=schemas.CommentBase)
def create_comment(comment: schemas.CommentBase, db: Session=Depends(get_bd)):
	'插入comment数据'
	print(comment.dict())
	print(type(comment))
	return curd.create_comment(db=db, comment=comment)

@app.get("/commnet/{article_id}")
def read_comment(article_id: int, db: Session=Depends(get_bd)):
	'根据article_id查询comment数据'
	print("article_id = {}".format(article_id))
	print(type(article_id))
	db_comment = curd.get_comment_by_article_id(db, article_id=article_id)
	print("db_comment = {}".format(db_comment))
	if db_comment is None:
		raise HTTPException(status_code=404, detail="commnet not found")
	return db_comment