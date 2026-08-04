class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=len(nums)//3
        dici={}
        l1=[]
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        
        for key,value in dici.items():

            if value>l:

                l1.append(key)
        return l1