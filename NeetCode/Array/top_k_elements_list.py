from typing import List, Optional, Any, Tuple
from collections import defaultdict

# using prefix sum
class Solution:
  def topkfreq(self, nums: List[int], k: int) -> List[int]:
    
    freq = defaultdict()

    for num in nums:
      freq[num] = 1 + freq.get(num, 0)

    sort_values = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))

    res = list(sort_values.keys())[0:k]
    
    return res


if __name__ == "__main__":
  sol = Solution()
  nums = [int(x) for x in input().split()]

  k = int(input())

  print(sol.topkfreq(nums, k))