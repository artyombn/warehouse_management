from abc import ABC, abstractmethod

# Для управления транзакциями и работой с продуктами
# __enter__ и __exit__ внутри идут с with --> автоматический rollback() при ошибке


class UnitOfWork(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
