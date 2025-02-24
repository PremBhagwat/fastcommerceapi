# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://root:Prem@2403@localhost/ecommerce"  

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Function to create the database tables
# def init_db():
#     Base.metadata.create_all(bind=engine)







from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MySQL Database credentials
DB_USERNAME = "root"
DB_PASSWORD = "Prem%402403"  # @ is encoded as %40

DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "ecommerce_db"

# MySQL Connection string
DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the engine that connects to the database
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the Base class for ORM models
Base = declarative_base()

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the database tables (this will create all tables from models that inherit Base)
def create_db():
    Base.metadata.create_all(bind=engine)
