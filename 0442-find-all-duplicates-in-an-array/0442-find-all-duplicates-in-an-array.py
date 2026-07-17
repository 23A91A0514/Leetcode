class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        c=Counter(nums)
        for key,count in c.items():
            if count>=2:
                l.append(key)
        return l
        