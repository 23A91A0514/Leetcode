class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)

        min_index = nums.index(mini)
        max_index = nums.index(maxi)

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        left = max_index + 1
        right = len(nums) - min_index
        both = min_index + 1 + len(nums) - max_index

        return min(left, right, both)
        