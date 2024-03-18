from dataclasses import dataclass
from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


class Warehouse:
    def __init__(self) -> None:
        self.catalogue: list[Entry] = []

