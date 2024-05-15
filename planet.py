import math
from star import star

G = 6.67*(10**-11)

class planet():
  """
  Planet class

  Args:
    min (float): The minimum value of flux
    orbit(float): The number of days it takes to orbit it's star
    density(float): 
    mass(float): The mass of the planet in kg
    radius(float): Radius of planet in meter
  """

  def __init__(
    self,
    star: star,
    orbital_period: float = 0, # Unit
    density: float = 0, # Unit
    mass: float = 0, # in kg
    radius: float = 0, # meters
    orbital_radius: float = 0, # 
    velocity: float = 0, # m/s
  ) -> None:
    """
    Planet class

    Args:
      min(float): The minimum value of flux
      orbital_period(float): The number of seconds it takes to orbit it's star
      density(float): 
      mass(float):
      radius(float):
      velocity(float): Orbital velocity in m/s 
    """
    self.orbital_period = orbital_period
    self.density = density
    self.mass = mass
    self.radius = radius
    self.orbital_radius = orbital_radius
    self.star = star
    self.velocity = velocity

  def find_orbital_radius(self) -> float:
    """
    Find the orbital radius of planet, given the orbital period of the planet and the mass of the star
    """

    if self.orbital_period == 0:
      print("WARNING: You may not use this function before orbital_period is defined")
      return -1
    
    radius = G * self.star.mass * (self.orbital_period**2)
    radius /= 4 * (math.pi**2)
    radius **= (1/3)
    self.orbital_radius = radius
    return radius

  def find_mass(self) -> float:
    """
    Find the mass of the planet with the mass via MV = mv

    :returns: Mass of the planet
    """
    # MV = mv
    pl_mass = self.star.mass * self.star.wobble
    pl_mass /= self.velocity
    self.mass = pl_mass
    return pl_mass

  def find_radius(self) -> float:
    radius = (self.star.delta_flux)**0.5 * self.star.radius
    self.radius = radius
    return radius

  def find_density(self) -> float:
    """ 
    """
    density = self.mass / self.radius
    self.density = density
    return density

  def find_velocity(self) -> float:
    """
    Find the velocity :D

    :returns: Velocity in m/s
    """
    # (2*pi*orbital_radius) / orbital period
    v = 2 * math.pi * self.orbital_radius
    v /= self.orbital_period
    self.velocity = v
    return v