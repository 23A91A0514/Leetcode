class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        s = 0
        min_len = float('inf')

        for right in range(n):
            s += nums[right]

            while s >= target:
                min_len = min(min_len, right - left + 1)
                s -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
                


