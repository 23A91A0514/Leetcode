from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = permutations(nums)
        
        answer = []
        
        for p in result:
            answer.append(list(p))
        
        return answer