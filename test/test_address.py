from src.address import Address
from src.countries import Country

def test_if_country_in_list_of_country():
    anna_address = Address("50", "Vrijdagmarkt", "Gent", "900", Country.BELGIUM)
    assert anna_address.country in Country
