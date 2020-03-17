from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:lpb1987@127.0.0.1:3306/comment"

# 创建引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 创建session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 通过它来创建模块
Base = declarative_base()