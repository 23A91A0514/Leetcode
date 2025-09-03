class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Count characters in both strings and compare
        from collections import Counter
        return Counter(s) == Counter(t)
