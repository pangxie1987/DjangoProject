'''
定义调用 API 的时候需要返回的字段
'''

from typing import List
from pydantic import BaseModel

class CommentBase(BaseModel):
	'共有属性'
	article_id: int
	from_user_id: str
	to_user_id: str
	content: str
	nickname: str
	avatar_img: str