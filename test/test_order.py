from src.order import Item, Order
from src.product import Product
from src.countries import Country
from src.warehouse import Warehouse
from src.address import Address

from test.warehouse_build import build_warehouse

import pytest

guitar_gibson = Product(1, "Gibson Les Paul", 229)
guitar_fender = Product(2, "Fender Stratocaster", 450)
accoustic_guitar = Product(3, "Accoustic Guitar", 100)
eletric_amp = Product(4, "Eletric Amp", 50)
bass = Product(5, "Pink Bass", 180)

first_item = Item(guitar_gibson, 2)
second_item = Item(guitar_fender, 1)
third_item = Item(eletric_amp, 3)
fourth_item = Item(accoustic_guitar, 1)
fifth_item = Item(eletric_amp, 1)
sixth_item = Item(bass, 1)

tijs_address = Address("50", "Vrijdagmarkt", "Gent", "9000", Country.BELGIUM)
igor_address = Address("11", "Oblast", "Dnipro", "49000", Country.UKRAINE)
lorenzo_address = Address("234", "Viale Emilio Alemagna", "Milan", "201221", Country.ITALY)

def test_order_is_initialised_empty():
    order = Order(address=igor_address)
    assert order.order_items == {}

def test_if_updates_final_quantity():
    order = Order(address=lorenzo_address)
    order.add_item(first_item)
    order.add_item(second_item)
    order.add_item(first_item)
    assert order.order_items[first_item.product.description].quantity == 4

def test_update_warehouse_stock():
    warehouse = build_warehouse()
    order = Order(address=tijs_address)
    order.add_item(third_item)
    order.check_stock(warehouse=warehouse)
    assert warehouse.catalogue[third_item.product.description].stock == 67 #70 eletric amps in stock - 3 items in order

def test_final_price_without_shipping():
    warehouse = build_warehouse()
    order3 = Order(address=igor_address)
    order3.add_item(fourth_item)
    order3.add_item(fifth_item)
    order3.check_stock(warehouse=warehouse)
    product_price = order3.get_final_product_price()
    assert product_price == 150

def test_when_item_is_not_in_stock():
    warehouse = build_warehouse()
    order4 = Order(address=tijs_address)
    order4.add_item(sixth_item)
    with pytest.raises(Exception) as e:
        order4.check_stock(warehouse=warehouse)
    error_message = str(e.value)
    assert error_message == "Product not found in stock"
