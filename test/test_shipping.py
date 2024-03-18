from src.countries import Country
from src.shipping import calculate_shipping

def test_when_uk_region_order_higher_than_hundred():
    uk = Country.UNITED_KINGDOM.value
    shipping = calculate_shipping(country=uk, order_total=101)
    assert shipping == 0.0
