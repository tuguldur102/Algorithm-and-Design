from typing import List, Any, Optional
from collections import defaultdict

class Solution:
  key = "#"

  def encode(self, strs: List[str]) -> str:
    res_str = "#"

    for s in strs:
      res_str += s + self.key

    return res_str

  def decode(self, s: str) -> List[str]:
    
    lst = []
    pref = 0
    
    for i, c in enumerate(s):
      if c == self.key:
        lst.append(s[i - pref + 1: i])
        pref = 0

      pref += 1
    lst.remove('')

    return lst


if __name__ == "__main__":
  sol = Solution()

  strs = [str(x) for x in input().split()]
  
  print(sol.encode(strs))
  print(sol.decode(sol.encode(strs)))