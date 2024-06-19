from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False
    
if __name__ == "__main__":

    nums = [x for x in input().split()]

    s = Solution()
    print(s.hasDuplicate(nums))