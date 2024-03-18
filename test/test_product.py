from src.product import Product

def test_product_description():
    eletric_guitar = Product(1, "Gibson Les Paul", 229)
    assert eletric_guitar.description == "Gibson Les Paul"

def test_product_price():
    bass = Product(2, "bass", 150)
    assert bass.price == 150
