from abc import ABC, abstractmethod
from typing import List

from .models import Order, Product

# Репозиторий отвечает за сохранение, получение и удаление объектов из хранилища данных


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        pass

    @abstractmethod
    def get(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list(self) -> List[Product]:
        pass

    @abstractmethod
    def update(self, product: Product):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order):
        pass

    @abstractmethod
    def get(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def list(self) -> List[Order]:
        pass

    @abstractmethod
    def update(self, order: Order):
        pass

    @abstractmethod
    def delete(self, order_id: int):
        pass
