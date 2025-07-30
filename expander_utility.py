from typing import List

class StringExpander:
  def expand(self, input: str) -> List[int]:

    # base case: return empty array if input is empty
    if not input:
      return []
    
    result = []

    # clean whitespace and empty strings
    segments = [s.strip() for s in input.split(",") if s.strip()]

    for segment in segments:
      # check for "-" dash to extend integer
      if "-" in segment:
        range_start, range_end = segment.split("-")
        start, end = int(range_start), int(range_end)
        result.extend(range(start, end + 1))
      else:
        # simple number -> convert to integer
        result.append(int(segment))

    return result

if __name__ == '__main__':
  e = StringExpander
  input = " , 1 -3 , ,5 "
  print(e.expand(e, input))