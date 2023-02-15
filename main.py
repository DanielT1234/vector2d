import math
class Vector2d:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __repr__(self):
    return f"Vector2d(x='{self.x}', y={self.y})"
  def __str__(self):
    return f"{self.x}:{self.y}"
  def __abs__(self):
    leg1=self.x**2
    leg2=self.y**2
    legs=leg1+leg2
    return math.sqrt(legs)
    