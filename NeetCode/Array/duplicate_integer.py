from typing import List

class Solution:
  def hasDiplicate(self, nums: List[int]) -> bool:
    
    result = set()

    for num in nums:

      if num in result:
        return True
      
      result.add(num)
  
    return False
  
if __name__ == "__main__":
  nums = [int(x) for x in input().split()]

  sol = Solution()

  print(sol.hasDiplicate(nums))