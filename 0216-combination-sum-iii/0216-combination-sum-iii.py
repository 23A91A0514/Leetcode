from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr=[1,2,3,4,5,6,7,8,9]
        ans=[]
        for par in combinations(arr,k):
            if sum(par)==n:
                ans.append(par)

        return ans