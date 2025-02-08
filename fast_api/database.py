from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
DATABASE_URL = "mysql+pymysql://root@localhost/medimeet_db"

# Create an engine instance
engine = create_engine(DATABASE_URL, echo=True)

# Define Base
Base = declarative_base()

# Create session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()