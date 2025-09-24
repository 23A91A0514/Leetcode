from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_counter = Counter(nums1)
        ans = []
        for c in nums2:
            if c in n1_counter and n1_counter[c]>0:
                ans.append(c)
                n1_counter[c] -= 1            
        return ans
