from dataclasses import dataclass, field
from typing import List, Optional

# В чистой архитектуре все модели должны быть независимы от внешних зависимостей (БД, ORM)

@dataclass
class Product:
    id: Optional[int]
    name: str
    quantity: int
    price: float

    def is_in_stock(self) -> bool:
        return self.quantity > 0


@dataclass
class Order:
    id: Optional[int]
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)