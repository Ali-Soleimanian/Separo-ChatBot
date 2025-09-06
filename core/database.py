from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, text
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    api_key = Column(String, nullable=True)
    registration_date = Column(DateTime, default=datetime.utcnow)

def setup_db():
    engine = create_engine("sqlite:///data.db")
    Base.metadata.create_all(engine)
    
    try:
        with engine.connect() as conn:
            result = conn.execute(text("PRAGMA table_info(users)"))
            columns = [row[1] for row in result.fetchall()]
            if 'api_key' not in columns:
                conn.execute(text("ALTER TABLE users ADD COLUMN api_key TEXT"))
                conn.commit()
    except Exception as e:
        print(f"Database migration warning: {e}")
    
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()