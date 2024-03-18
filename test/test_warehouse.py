from src.warehouse import Entry, Warehouse
from src.product import Product
from test.product_builder import (
    guitar_fender,
    guitar_gibson,
    accoustic_guitar,
    eletric_amp
)


first_entry = Entry(guitar_gibson, 40)
second_entry = Entry(guitar_fender, 20)
third_entry = Entry(accoustic_guitar, 15)
fourth_entry = Entry(eletric_amp, 15)
def test_if_entry_returns_product_description():
    assert first_entry.product.description == "Gibson Les Paul"

def test_if_entry_returns_stock():
    assert second_entry.stock == 20

def test_if_catalogue_is_initialised_empty():
    warehouse = Warehouse()
    assert len(warehouse.catalogue) == 0

def test_if_catalogue_has_unique_entry_and_updates_stock_when_multiple_entry():
    warehouse = Warehouse()
    warehouse.add_entry(first_entry)
    warehouse.add_entry(second_entry)
    warehouse.add_entry(third_entry)
    warehouse.add_entry(third_entry)
    assert len(warehouse.catalogue) == 3
    assert warehouse.catalogue[third_entry.product.description].stock == 30
