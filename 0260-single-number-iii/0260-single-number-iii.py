class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        # Find numbers with frequency 1
        for num, count in freq.items():
            if count == 1:
                ans.append(num)

        return ans