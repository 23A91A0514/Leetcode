from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        for p in combinations(range(1, n + 1), k):
            ans.append(list(p))

        return ans
      
        

        