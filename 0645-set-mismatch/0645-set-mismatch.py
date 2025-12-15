from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l1=[]
        c=Counter(nums)

        for num,count in c.items():
            if count>1:
                l1.append(num)

        for i in range(1,len(nums)+1):
            if i  not in c:
                l1.append(i)
        return l1

        