from src.warehouse import Warehouse, Entry
from src.product import Product

#products
guitar_gibson = Product(1, "Gibson Les Paul", 229)
guitar_fender = Product(2, "Fender Stratocaster", 450)
accoustic_guitar = Product(3, "Accoustic Guitar", 100)
eletric_amp = Product(4, "Eletric Amp", 50)

#stock entries
first_entry = Entry(guitar_gibson, 40)
second_entry = Entry(guitar_fender, 10)
third_entry = Entry(accoustic_guitar, 15)
fourth_entry = Entry(eletric_amp, 70)


def build_warehouse() -> Warehouse:
    warehouse = Warehouse()
    warehouse.add_entry(first_entry)
    warehouse.add_entry(second_entry)
    warehouse.add_entry(third_entry)
    warehouse.add_entry(fourth_entry)
    return warehouse
