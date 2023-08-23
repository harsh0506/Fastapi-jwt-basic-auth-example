from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DBURL")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__  = "users_auth_resoluteai"
    id = Column(Integer , primary_key = True,index=True)
    name = Column(String ,unique = True )
    hashed_password = Column(String)