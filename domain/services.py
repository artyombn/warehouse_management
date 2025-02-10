from typing import List

from .models import Order, Product
from .repositories import OrderRepository, ProductRepository


class WarehouseService:
    def __init__(self, product_repo: ProductRepository, order_repo: OrderRepository):
        self.product_repo = product_repo
        self.order_repo = order_repo

    def create_product(self, name: str, quantity: int, price: float) -> Product:
        product = Product(id=None, name=name, quantity=quantity, price=price)
        self.product_repo.add(product)
        return product

    def get_product(self, product_id: int) -> Product:
        return self.product_repo.get(product_id)

    def get_product_list(self):
        return self.product_repo.list()

    def update_product(
        self, product_id: int, name: str, quantity: int, price: float
    ) -> Product:
        product = Product(id=product_id, name=name, quantity=quantity, price=price)
        self.product_repo.update(product)
        return self.product_repo.get(product_id)

    def delete_product(self, product_id: int):
        return self.product_repo.delete(product_id)

    def create_order(self, products: List[Product]) -> Order:
        order = Order(id=None, products=products)
        self.order_repo.add(order)
        return order

    def get_order(self, order_id: int) -> Order:
        return self.order_repo.get(order_id)

    def get_order_list(self):
        return self.order_repo.list()

    def update_order(self, order_id: int, products: List[Product]) -> Order:
        order = Order(id=order_id, products=products)
        self.order_repo.update(order)
        return self.order_repo.get(order_id)

    def delete_order(self, order_id: int):
        return self.order_repo.delete(order_id)
