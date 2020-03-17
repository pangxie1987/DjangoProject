'''
通过 Base 来创建数据表相应的类
'''

from databases import Base
from sqlalchemy import Column, Integer, String, DateTime

class Comment(Base):
	__tablename__ = "comment"
	id = Column(Integer, primary_key=True, index=True)
	article_id = Column(Integer)
	create_at = Column(DateTime)
	from_user_id = Column(String(32))
	to_user_id = Column(String(32))
	content = Column(String(128))
	nickname = Column(String(32))
	avatar_img = Column(String(32))

class Article(Base):
	__tablename__ = "article"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(128))