from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    api_key = Column(String, nullable=True)  # Store user's API key
    registration_date = Column(DateTime, default=datetime.utcnow)

def setup_db():
    engine = create_engine("sqlite:///data.db")
    Base.metadata.create_all(engine)
    
    # Handle database migrations for existing databases
    try:
        with engine.connect() as conn:
            # Check if api_key column exists, if not add it
            result = conn.execute("PRAGMA table_info(users)")
            columns = [row[1] for row in result.fetchall()]
            if 'api_key' not in columns:
                conn.execute("ALTER TABLE users ADD COLUMN api_key TEXT")
                conn.commit()
    except Exception as e:
        print(f"Database migration warning: {e}")
    
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()