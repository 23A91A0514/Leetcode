from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxi = float('-inf')  # Start at negative infinity to handle all-negative arrays
        
        for i in range(len(nums)):
            s += nums[i]
            
            # Always update maxi if our current running sum is larger
            if s > maxi:
                maxi = s
                
            # If our running sum drops below zero, it's useless. Reset it.
            if s < 0:
                s = 0
                
        return maxi