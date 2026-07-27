class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_left = nums[0]
        ans = float('-inf')

        for j in range(k, n):
            max_left = max(max_left, nums[j - k])
            ans = max(ans, max_left + nums[j])

        return ans