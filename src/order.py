from dataclasses import dataclass
from typing import Dict, List

from src.address import Address
from src.product import Product
from src.shipping import calculate_shipping
from src.warehouse import Warehouse


@dataclass
class Item:
    product: Product
    quantity: int


@dataclass
class Order:
    def __init__(self, address: Address) -> None:
        self.address: Address = address
        self.order_items: Dict[str, Item] = {}
        self.checkout_order: List() = []

    def add_item(self, item: Item) -> None:
        if item.product.description not in self.order_items.keys():
            self.order_items[item.product.description] = item
        else:
            self.order_items[item.product.description].quantity += item.quantity

    def check_stock(self, warehouse: Warehouse) -> None:
        for product_name, order_item in self.order_items.items():
            if product_name in warehouse.catalogue.keys():
                if order_item.quantity > warehouse.catalogue[product_name].stock:
                    raise Exception("Product quantity not available in stock")
                warehouse.catalogue[product_name].stock -= order_item.quantity
                self.checkout_order.append(order_item)
            else:
                raise Exception("Product not found in stock")
    
    def get_final_product_price(self) -> float:
        return sum(
            (item.quantity) * (item.product.price) for item in self.checkout_order
        )
    
    def get_shipping_fee(self) -> float:
        country = self.address.country.value
        order_total = self.get_final_product_price()
        return calculate_shipping(country=country, order_total=order_total)

    def get_total(self) -> float:
        return (
            self.get_shipping_fee() + self.get_final_product_price()
        )