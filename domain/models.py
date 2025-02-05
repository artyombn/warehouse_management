from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    quantity: int
    price: float
    id: int | None = None

@dataclass
class Order:
    products: List[Product] = field(default_factory=list)
    id: int | None = None

    def add_product(self, product: Product):
        self.products.append(product)