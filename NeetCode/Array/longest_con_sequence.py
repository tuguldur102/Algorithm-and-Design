from typing import List, Optional, Any, Tuple
from collections import defaultdict

class Solution:
  def longest_con_seq(self,
                      nums: List[int]) -> int:
    
    d = defaultdict(int)
    max_length = 0

    for num in nums:

      if num not in d:
        # Retreive current length steaks from left and right sides
        left_number = d.get(num - 1, 0)
        right_number = d.get(num + 1, 0)

        
        current_length = left_number + 1 + right_number

        d[num] = current_length
        max_length = max(max_length, current_length)

        # Update the left and right sides
        d[num - left_number] = current_length
        d[num + right_number] = current_length

    return max_length
  
if __name__ == "__main__":
  sol = Solution()

  nums = [int(x) for x in input().split()]

  print(sol.longest_con_seq(nums))