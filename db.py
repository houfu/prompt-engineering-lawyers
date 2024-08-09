from contextlib import contextmanager

from sqlmodel import SQLModel, create_engine, Session

import models

from settings import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)
SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Session:
    """Creates a context with an open SQLAlchemy async session."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
