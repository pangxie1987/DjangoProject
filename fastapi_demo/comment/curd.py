'''
定义数据库操作方法
'''
from sqlalchemy.orm import Session
# from . import models, schemas
import models, schemas

def get_comment(db: Session, comment_id: int):
	'根据评论id获取评论数据'
	return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_comment_by_article_id(db: Session, article_id: int):
	'根据文章id获取评论'
	# return db.query(models.Comment).filter(models.Comment.article_id == article_id).first()	# 返回第一条
	return db.query(models.Comment).filter(models.Comment.article_id == article_id).order_by(models.Comment.create_at).all()		# 返回所有数据

def create_comment(db: Session, comment: schemas.CommentBase):
	'插入评论表'
	print(comment)
	db_comment = models.Comment(**comment.dict())
	db.add(db_comment)
	db.commit()
	db.refresh(db_comment)
	return db_comment