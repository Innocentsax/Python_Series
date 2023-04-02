import pytest

# Using doctest
def square(x: float) -> float:
  """Doctest for the square of a number.
  >>> square(5)
  25
  >>> square(0)
  0
  """
  return x * x

# Using Pytest
@pytest.mark.parametrize(
    ('n', 'expected'),
    (
      (0, 0),
      (5, 25),
      
    ),
)
def test_square(n, expected):
  assert square(n) == expected
