from typing import List
import re
from config import DELIMITERS

class StringExpander:
  def __init__(self, delimiters=None):
    # set delimiters from instance or on fallback use from config
    self.delimiters = delimiters or DELIMITERS
    # pattern for splitting
    self.delimiter_pattern = "|".join([re.escape(d) for d in sorted(self.delimiters, key=len, reverse=True)])


  def expand(self, input: str) -> List[int]:
    # base case: return empty array if input is empty
    if not input:
      return []
    
    result = []

    # clean whitespace and empty strings
    segments = [s.strip() for s in input.split(",") if s.strip()]

    for segment in segments:
      # check for delimiter to extend integer
      parts = re.split(self.delimiter_pattern, segment)
      if len(parts) == 1:
        # single number
        result.append(self.validate_int(parts[0]))
      elif len(parts) == 2:
        # number range
        start = self.validate_int(parts[0])
        end = self.validate_int(parts[1])
        step = 1 if start <= end else -1
        result.extend(range(start, end + step, step))
      else:
        # invalid format - throw error
        raise ValueError(f"Invalid format: '{segment}'")

    return result

  def validate_int(self, value: str) -> int:
    value = value.strip()
    if not re.fullmatch(r"-?\d+", value):
      raise ValueError(f"Invalid number: '{value}'")
    return int(value)

if __name__ == '__main__':
  e = StringExpander(delimiters=['.'])
  input = "5.5"
  print(e.expand(input))