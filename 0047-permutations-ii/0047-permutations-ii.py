from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = permutations(nums)
        
        answer = set()
        
        for p in result:
            answer.add(p)
        
        final_answer = []
        
        for p in answer:
            final_answer.append(list(p))
        
        return final_answer