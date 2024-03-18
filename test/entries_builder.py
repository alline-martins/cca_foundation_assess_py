from src.warehouse import Entry
from test.product_builder import (
    guitar_fender,
    guitar_gibson,
    accoustic_guitar,
    eletric_amp
)

first_entry = Entry(guitar_gibson, 40)
second_entry = Entry(guitar_fender, 20)
third_entry = Entry(accoustic_guitar, 15)
fourth_entry = Entry(eletric_amp, 15)