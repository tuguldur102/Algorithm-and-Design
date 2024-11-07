from typing import List
from collections import defaultdict

class Solution:
  def group_anagram(self, strs: List[str]) -> List[List[str]]:

    res = defaultdict(list)

    for s in strs:
      count = 0
      for c in s:
        count += ord(c)
      
      res[count].append(s)

    return res.values()

if __name__ == "__main__":
  strs = [str(s) for s in input().split()]

  sol = Solution()

  print(sol.group_anagram(strs=strs))
