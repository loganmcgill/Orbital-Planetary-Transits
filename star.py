class star():
  """
  Star Class
  """
  def __init__(
    self, 
    mass: float, 
    radius: float,
    wobble: float,
    delta_flux: float
  ) -> None:
    """
    Initalize a star object
    
    :param mass: Mass of star in kg
    :param radius: Radius of star in meters
    :param wobble: Wobble of star in m/s
    """
    self.mass = mass
    self.radius = radius
    self.wobble = wobble
    self.delta_flux = delta_flux