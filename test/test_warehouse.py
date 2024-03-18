from src.warehouse import Entry
from src.product import Product

guitar_gibson = Product(1, "Gibson Les Paul", 229)
guitar_fender = Product(2, "Fender Stratocaster", 450)
accoustic_guitar = Product(3, "Accoustic Guitar", 100)
eletric_amp = Product(4, "Eletric Amp", 50)

def test_if_entry_returns_product_description():
    first_entry = Entry(guitar_gibson, 40)
    assert first_entry.product.description == "Gibson Les Paul"

def test_if_entry_returns_stock():
    second_entry = Entry(guitar_fender, 20)
    assert second_entry.stock == 20
