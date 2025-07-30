import unittest
from expander_utility import StringExpander
from config import DELIMITERS

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

  # test multiple empty strings
  def test_multiple_empty_strings(self):
    self.assertEqual(self.string_expander.expand(" , , , "), [])

  # test leading or traling whitespace around data
  def test_whitespace_string(self):
    self.assertEqual(self.string_expander.expand(" 2, 3 - 4,   5, ,"), [2, 3, 4, 5])

  # test delimiters from config.py
  def test_config_delimiters(self):
    self.assertEqual(self.string_expander.expand("1-2, 4..6,   , 7~8, 9 to 11"), [1, 2, 4, 5, 6, 7, 8, 9, 10, 11])

  # test custom delimiters
  def test_custom_delimiters(self):
    expander = StringExpander(delimiters=["*"])
    self.assertEqual(expander.expand("2*5"), [2, 3, 4, 5])

  # test format error
  def test_format_error(self):
    with self.assertRaises(ValueError):
      self.string_expander.expand("1-2-5")

  # test delimiter error
  def test_delimiter_change_error(self):
    expander = StringExpander(delimiters=["*"])
    with self.assertRaises(ValueError):
      expander.expand("1-2")

  # test reverse range expand
  def test_reverse_range(self):
    self.assertEqual(self.string_expander.expand("5-3"), [5, 4, 3])

  # test single number range
  def test_single_number_range(self):
    self.assertEqual(self.string_expander.expand("5-5"), [5])

  # test of validation of numeric value
  def test_numeric_validation(self):
    with self.assertRaises(ValueError):
      self.string_expander.expand("6-t")

if __name__ == '__main__':
  unittest.main()