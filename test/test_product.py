from src.product import Product

import pytest

@pytest.mark.parametrize("id, description, price, expected_value", [
    (1, "Gibson Les Paul", 229, "Gibson Les Paul"),
    (2, "Fender Stratocaster", 450, "Fender Stratocaster"),
    (3, "Accoustic Guitar", 100, "Accoustic Guitar"),
    (4, "Eletric Amp", 50, "Eletric Amp")
])
def test_product_description(id, description, price, expected_value):
    product = Product(id=id, description=description, price=price)
    assert product.description == expected_value

def test_product_price():
    bass = Product(2, "bass", 150)
    assert bass.price == 150

def test_product_id():
    accoustic_guitar = Product(3, "Accoustic Guitar", 100)
    assert accoustic_guitar.id == 3
