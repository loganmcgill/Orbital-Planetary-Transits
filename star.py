import math
import numpy

class star():
  """
  Star Class
  """
  def __init__(
    self, 
    mass: float, 
    radius: float,
    wobble: float
  ) -> None:
    """
    Initalize a star object
    
    :param mass: Mass of star in kg
    :param radius: Radius of star in meters
    """
    self.mass = mass
    self.radius = radius
    self.wobble = wobble

  
    