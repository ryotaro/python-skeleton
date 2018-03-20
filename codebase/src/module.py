class Adder:
  def __init__(self, fixed_val):
    self.fixed_val = fixed_val

  def add(self, rhs):
    return self.fixed_val + rhs