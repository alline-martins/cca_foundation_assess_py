from src.address import Address
from src.countries import Country

def test_if_country_in_list_of_country():
    anna_address = Address("50", "Vrijdagmarkt", "Gent", "900", Country.BELGIUM)
    assert anna_address.country in Country

def test_address_city():
    john_address = Address("234", "Viale Emilio Alemagna", "Milan", "201221", Country.ITALY)
    assert john_address.city == "Milan"
