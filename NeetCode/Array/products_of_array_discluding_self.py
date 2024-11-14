from typing import List, Any, Optional
from collections import defaultdict

class Solution:
  def productExceptself(self, nums: List[int]) -> List[int]:
    
    # Axiom of identity element in product of Field thoery
    all_prod = 1

    zero_flag = False

    for num in nums:
      if num != 0:
        all_prod *= num
      else:
        zero_flag = True
      
    res_container = [all_prod] * len(nums)

    if not zero_flag:
      for i, num in enumerate(nums):
        if num != 0:
          res_container[i] //= num      
    # -1 0 1 2 3
    # -6 -6 -6 -6 -6
    # 0 -6 0 0 0
    else:
      for i, num in enumerate(nums):
        if num == 0:
          res_container[i] = all_prod
        else:
          res_container[i] = 0

    return res_container
  
  def optimal(self, nums: List[int]) -> List[int]:
    n = len(nums)

    res = [0] * n
    pref = [0] * n
    suff = [0] * n

    pref[0] = suff[n - 1] = 1

    for i in range(1, n):
      pref[i] = nums[i - 1] * pref[i - 1]
    for i in range(n - 2, - 1, -1):
      suff[i] = nums[i + 1] * suff[i + 1]
    
    print(f"Pref: {pref}")
    print(f"Suff: {suff}")

    for i in range(n):
      res[i] = pref[i] * suff[i]
    
    return res

if __name__ == "__main__":
  sol = Solution()

  nums = [int(x) for x in input().split()]

  print(sol.productExceptself(nums))
  print(sol.optimal(nums))