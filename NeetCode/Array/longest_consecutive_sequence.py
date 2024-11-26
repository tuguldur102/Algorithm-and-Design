from typing import List, Optional, Tuple, Any
from collections import defaultdict

class Solution:
  def longest_con(self, nums: List[int]) -> int:
    bag = set(nums)
    longest = 0

    for num in nums:
      prev = num - 1
      if prev not in bag:
        length = 0
        while (num + length) in bag:
          length += 1
          longest = max(length, longest)

    return longest

  def longest_con_hashmap(self, num: List[int]) -> int:
    hashmap = defaultdict(int)
    res = 0

    for num in nums:
      if not hashmap[num]:
        hashmap[num] = hashmap[num - 1] + hashmap[num + 1] + 1
        hashmap[num - hashmap[num - 1]] = hashmap[num]
        hashmap[num + hashmap[num + 1]] = hashmap[num]
        res = max(res, hashmap[num])

    return hashmap[num]

if __name__ == "__main__":
  sol = Solution()

  # nums = [int(x) for x in input().split()]

  nums = [0,3,2,5,4,6,1,1]
  print(sol.longest_con(nums))
  print(sol.longest_con_hashmap(nums))
  