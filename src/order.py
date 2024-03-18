from dataclasses import dataclass

from src.address import Address
from src.product import Product


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    def __init__(self, address: Address) -> None:
        self.address = Address
        self.order_items: list[Item] = []

    def add_item(self, items: list[Item]) -> None:
        self.order_items.append(items)