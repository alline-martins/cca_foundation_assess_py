from src.product import Product

def test_product_description():
    eletric_guitar = Product(1, "Gibson Les Paul", 229)
    assert eletric_guitar.description == "Gibson Les Paul"
