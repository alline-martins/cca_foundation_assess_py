from src.order import Item, Order
from src.product import Product
from src.countries import Country
from src.warehouse import Warehouse
from src.address import Address


guitar_gibson = Product(1, "Gibson Les Paul", 229)
guitar_fender = Product(2, "Fender Stratocaster", 450)
accoustic_guitar = Product(3, "Accoustic Guitar", 100)
eletric_amp = Product(4, "Eletric Amp", 50)

first_item = Item(guitar_gibson, 2)
second_item = Item(guitar_fender, 1)
third_item = Item(eletric_amp, 3)

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

