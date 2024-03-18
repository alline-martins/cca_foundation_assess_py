from dataclasses import dataclass
from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


class Warehouse:
    def __init__(self) -> None:
        self.catalogue: dict[str, Entry] = {}
    
    def add_entry(self, entry: Entry) -> None:
        #check if already exist
        if entry.product.description not in self.catalogue.keys():
            self.catalogue[entry.product.description] = entry
        else:
            print("Entry already exists")

