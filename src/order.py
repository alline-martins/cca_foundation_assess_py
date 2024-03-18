from dataclasses import dataclass
from typing import Dict, List

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
        self.order_items: Dict[str, Item] = {}

    def add_item(self, item: Item) -> None:
        if item.product.description not in self.order_items.keys():
            self.order_items[item.product.description] = item
        else:
            print("Update quantity here")
