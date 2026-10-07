class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1 = 0
        c2 = 0
        s = s.lower()
        n = len(s)
        mid = n // 2  # Use integer division
        
        s1 = s[:mid]
        s2 = s[mid:]
        vowels = "aeiou"
        
        for i in range(mid):  # Loop up to the integer 'mid'
            if s1[i] in vowels:
                c1 += 1
            if s2[i] in vowels:
                c2 += 1
                
        return c1 == c2