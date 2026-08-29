class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find first occurrence
        lo = 0
        hi = len(nums) - 1
        first = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                first = mid
                hi = mid - 1       # Search towards left

            elif nums[mid] < target:
                lo = mid + 1

            else:
                hi = mid - 1

        # If target doesn't exist
        if first == -1:
            return [-1, -1]

        lo = 0
        hi = len(nums) - 1
        last = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                last = mid
                lo = mid + 1       

            elif nums[mid] < target:
                lo = mid + 1

            else:
                hi = mid - 1

        return [first, last]