class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        l1=[]
        for i in range(1,len(nums)+1):
            if i not in c:
                l1.append(i)
        return l1
          