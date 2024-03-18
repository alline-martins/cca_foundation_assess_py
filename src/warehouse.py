from dataclasses import dataclass
from src.product import Product


@dataclass
class Entry:
    product: Product
    stock: int


class Warehouse:
    def __init__(self) -> None:
        self.catalogue: list[Entry] = []
    
    def add_entry(self, entry: Entry) -> None:
        #check if already exist
        if entry not in self.catalogue:
            self.catalogue.append(entry)
        else:
            print("Entry already exists")

