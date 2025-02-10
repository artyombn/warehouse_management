import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.orm import Base


@pytest.fixture(scope="module")
def db_session():
    engine = create_engine("sqlite:///:memory:")
    SessionFactory = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = SessionFactory()

    yield session

    session.close()
    Base.metadata.drop_all(engine)
