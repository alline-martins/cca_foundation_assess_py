from src.warehouse import Entry, Warehouse
from src.product import Product
from test.entries_builder import (
    first_entry,
    second_entry,
    third_entry,
)

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
