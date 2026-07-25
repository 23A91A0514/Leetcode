from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i,val in c.items():
            if val==1:
                return i
        