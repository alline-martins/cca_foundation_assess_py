from src.warehouse import Warehouse, Entry
from src.product import Product
from test.product_builder import (
    guitar_fender,
    guitar_gibson,
    accoustic_guitar,
    eletric_amp,
    blue_drum
)

#stock entries
first_entry = Entry(guitar_gibson, 40)
second_entry = Entry(guitar_fender, 10)
third_entry = Entry(accoustic_guitar, 15)
fourth_entry = Entry(eletric_amp, 70)
fifth_entry = Entry(blue_drum, 0)


def build_warehouse() -> Warehouse:
    warehouse = Warehouse()
    warehouse.add_entry(first_entry)
    warehouse.add_entry(second_entry)
    warehouse.add_entry(third_entry)
    warehouse.add_entry(fourth_entry)
    warehouse.add_entry(fifth_entry)
    return warehouse
