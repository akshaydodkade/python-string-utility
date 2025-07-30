import unittest
from expander_utility import StringExpander

class TestExpander(unittest.TestCase):
  def setUp(self):
    self.string_expander = StringExpander()

  # test base condition
  def test_empty_string(self):
    self.assertEqual(self.string_expander.expand(""), [])

  # test single number
  def test_single_number(self):
    self.assertEqual(self.string_expander.expand("2"), [2])
  
  # test number range
  def test_string_range(self):
    self.assertEqual(self.string_expander.expand("3-5"), [3, 4, 5])

  # test combination of both number and range
  def test_combination(self):
    self.assertEqual(self.string_expander.expand("2,3-5"), [2, 3, 4, 5])

  # test empty strings
  def test_empty_string(self):
    self.assertEqual(self.string_expander.expand(" , , , "), [])

  # test leading or traling whitespace around data
  def test_empty_string(self):
    self.assertEqual(self.string_expander.expand(" 2, 3 - 4,   5, ,"), [2, 3, 4, 5])

if __name__ == '__main__':
  unittest.main()