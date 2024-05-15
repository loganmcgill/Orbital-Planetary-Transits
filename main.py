from planet import planet
from star import star
import math
import numpy as np

def sigs(num):
  return float(np.format_float_positional(num, precision=3, fractional=False, unique=True))

#test_star = star(2*(10**30), 696340000)
test_star = star(mass=0.854 * 2*(10**30), radius=0.768 * 696340000, wobble=80)

test = planet(
  test_star,
  orbital_period = 5.5 * 10**5,
  delta_flux = 0.015
)

print(f"Orbital Radius is {sigs(test.find_orbital_radius()):.3e}")
print(f"Orbital Velocity is {sigs(test.find_velocity()):.3e}")
print(f"Mass is {sigs(test.find_mass()):.3e}")
print(f"Radius is {sigs(test.find_radius()):.3e}")
print(f"Density is {sigs(test.find_density()):.3e}")
