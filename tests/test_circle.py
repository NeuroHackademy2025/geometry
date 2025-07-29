from geometry.circle import calculate_area, calculate_circ
from math import pi

### This defines the area of a circle
def test_area():
    r = 1 
    area = calculate_area(r)
    assert area == pi, "The calculation is wrong"

### This defines the circumference of a circle
def test_circ():
    r = 1 
    circ = calculate_circ(r)
    assert circ == 2 * pi, "The calculation is wrong"
