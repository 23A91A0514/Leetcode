class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n

        for i in range(n):
            for j in range(1, n):
                k = (i + j) % n
                if nums[k] > nums[i]:
                    res[i] = nums[k]
                    break

        return res