import unittest
from expander_utility import StringExpander

class TestExpander(unittest.TestCase):
  def setUp(self):
    self.string_expander = StringExpander()

  # test base condition
  def test_empty_string(self):
    self.assertEqual(self.string_expander.expand(""), [])

  def test_single_number(self):
    self.assertEqual(self.string_expander.expand("2"), [2])
  
  def test_string_range(self):
    self.assertEqual(self.string_expander.expand("3-5"), [3, 4, 5])

  def test_combination(self):
    self.assertEqual(self.string_expander.expand("2,3-5"), [2, 3, 4, 5])

if __name__ == '__main__':
  unittest.main()