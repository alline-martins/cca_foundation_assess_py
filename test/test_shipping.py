from src.countries import Country
from src.shipping import calculate_shipping
import pytest

@pytest.mark.parametrize("country, order_total, expected_value",[
    (Country.UNITED_KINGDOM.value, 101, 0.0),
    (Country.UNITED_KINGDOM.value, 90, 4.99),
    (Country.BELGIUM.value, 150, 4.99),
    (Country.NETHERLANDS.value, 50, 8.99),
    (Country.UKRAINE.value, 100, 9.99),
    (Country.UKRAINE.value, 50, 9.99)
])
def test_shipping_calculater(country, order_total, expected_value):
    shipping = calculate_shipping(country=country, order_total=order_total)
    assert shipping == expected_value
