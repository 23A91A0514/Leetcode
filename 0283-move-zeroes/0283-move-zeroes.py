class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0  # position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap only if i != last_non_zero to avoid unnecessary operations
                if i != last_non_zero:
                    nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
