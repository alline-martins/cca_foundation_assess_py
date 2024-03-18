from src.countries import Country
from src.shipping import calculate_shipping
import pytest

@pytest.mark.parametrize("country, order_total, expected_value",[
    (Country.UNITED_KINGDOM.value, 121, 0.0),
    (Country.UNITED_KINGDOM.value, 110, 4.99),
    (Country.BELGIUM.value, 250, 5.99),
    (Country.NETHERLANDS.value, 190, 9.99),
    (Country.UKRAINE.value, 100, 9.99),
    (Country.UKRAINE.value, 50, 9.99)
])
def test_shipping_calculater(country, order_total, expected_value):
    shipping = calculate_shipping(country=country, order_total=order_total)
    assert shipping == expected_value
