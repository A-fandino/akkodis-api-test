import os
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

uri = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"


def generate_session():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.pool import NullPool

    engine = create_engine(
        uri,
        poolclass=NullPool,
    )
    return sessionmaker(autocommit=False, bind=engine)


SessionLocal = generate_session()
