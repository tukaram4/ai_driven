import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Database URL configuration
# Replace with your actual credentials or environment variable
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:Tukaram@2001@localhost:5432/E-Commerce"
)

# 2. Create the Engine
# Manages the physical connection pool to PostgreSQL
engine = create_engine(
    # For PostgreSQL, no special arguments are needed here
    SQLALCHEMY_DATABASE_URL
)

# 3. Create the SessionLocal factory
# Creates tailored, active database sessions on demand
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# 4. Create the Base class
# The registry and blueprint for your database models
Base = declarative_base()

# 5. Database Session Dependency
# Context manager for FastAPI endpoints to safely acquire and close connections
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
