from src.order import Item
from test.product_builder import (
    guitar_fender,
    guitar_gibson,
    eletric_amp,
    accoustic_guitar,
    bass,
    blue_drum
)


first_item = Item(guitar_gibson, 2)
second_item = Item(guitar_fender, 1)
third_item = Item(eletric_amp, 3)
fourth_item = Item(accoustic_guitar, 1)
fifth_item = Item(eletric_amp, 1)
sixth_item = Item(bass, 1)
seveth_item = Item(blue_drum, 1)