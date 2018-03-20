from ..src.module import Adder


import pytest
class TestModule:
  def test_adder_should_add_integer(self, anyint):
    adder = Adder(anyint)
    assert adder.add(1) == anyint + 1