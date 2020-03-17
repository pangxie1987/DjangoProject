'''
通过 Base 来创建数据表相应的类
'''

from .databases import Base
from sqlalchemy import Column, Integer, String, DateTime

class Comment(Base):
	__tablename__ = "commnet"
	id = Column(Integer, primary_key=True, index=True)
	article_id = Column(Integer)
	create_at = Column(DateTime)
	from_user_id = Column(String)
	to_user_id = Column(String)
	content = Column(String)
	nickname = Column(String)
	avatar_img = Column(String)

class Article(Base):
	__tablename__ = "article"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String)