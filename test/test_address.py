from src.address import Address
from src.countries import Country
import pytest
def test_if_country_in_list_of_country():
    anna_address = Address("50", "Vrijdagmarkt", "Gent", "900", Country.BELGIUM)
    assert anna_address.country in Country

@pytest.mark.parametrize("house, street, city, postcode, country, expected_country", [
    ("50", "Vrijdagmarkt", "Gent", "900", Country.BELGIUM,Country.BELGIUM ),
    ("11", "Holywell Close", "London", "SE3", Country.UNITED_KINGDOM, Country.UNITED_KINGDOM),
    ("123", "Vilae Emilio Alemganha", "Milan", "12414", Country.ITALY, Country.ITALY),
      
])
def test_address_city(house, street, city, postcode, country, expected_country):
    client_address = Address(house, street,city, postcode, country)
    assert client_address.country == expected_country
