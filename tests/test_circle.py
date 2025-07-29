from geometry.circle import calculate_area, calculate_circ
from math import pi


def test_area():
    r = 1 
    area = calculate_area(r)
    assert area == pi, "The calculation is wrong."

def test_circ():
    r = 1 
    circ = calculate_circ(r)
    assert circ == 2 * pi, "The calculation is wrong."
