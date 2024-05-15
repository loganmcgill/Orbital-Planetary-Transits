from planet import planet
from star import star

console_input = input("Input values relative to the Mass and Radius of Sun? [hell yeah / hell no] or (less cool) [Y/N]: ").lower()
if {"yes": True, "y": True, "ye": True, "hell yeah": True}.get(console_input):
  mass=2*(10**30) * float(input("Enter ratio of mass relative to the mass of the sun: "))
  radius=696340000 * float(input("Enter ratio of radius relative to the mass of the sun: "))
else:
  mass=float(input("Enter mass of Star in Kilograms: "))
  radius=float(input("Enter radius of Star in m: "))
  
wobble=float(input("Enter of wobble in meters per second: "))
delta_flux=float(input("Enter change in flux caused by a planetary transit: "))

test_star = star(mass=mass, radius=radius, wobble=wobble, delta_flux=delta_flux)

orbital_period = float(input("Enter orbital period of the planet in s: "))
test = planet(
  test_star,
  orbital_period = orbital_period
)

print(f"Orbital Radius is {test.find_orbital_radius():.3e} meters")
print(f"Orbital Velocity is {test.find_velocity():.3e} m/s")
print(f"Mass is {test.find_mass():.3e} kilograms")
print(f"Radius is {test.find_radius():.3e} meters")
print(f"Density is {test.find_density():.3e} kg/m^3")