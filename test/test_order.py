from src.order import Order
from src.countries import Country
from src.address import Address
from test.items_builder import (
    first_item,
    second_item,
    third_item,
    fourth_item,
    fifth_item,
    sixth_item,
    seveth_item
)
from test.warehouse_build import build_warehouse

import pytest


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

def test_when_quantity_is_higher_than_available_in_stock():
    warehouse = build_warehouse()
    order5 = Order(address=lorenzo_address)
    order5.add_item(seveth_item)
    with pytest.raises(Exception) as e:
        order5.check_stock(warehouse=warehouse)
    error_message = str(e.value)
    assert error_message == "Product quantity not available in stock"

def test_shipping_fee():
    warehouse = build_warehouse()
    order6 = Order(address=tijs_address)
    order6.add_item(third_item)
    order6.check_stock(warehouse=warehouse)
    shipping_fee = order6.get_shipping_fee()
    assert shipping_fee == 4.99
