class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums=[1,2,3]
        l=[[]]
        for num in nums:
            new = []

            for x in l:
                new.append(x + [num])

            l+=new

        return l