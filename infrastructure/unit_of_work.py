from sqlalchemy.orm import Session

from domain.unit_of_work import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session: Session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
