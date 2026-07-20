from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        con=Counter(nums)
        for key , value in con.items():
            if value>=2:
              ans+=(value*(value-1))//2
        return ans
        
        