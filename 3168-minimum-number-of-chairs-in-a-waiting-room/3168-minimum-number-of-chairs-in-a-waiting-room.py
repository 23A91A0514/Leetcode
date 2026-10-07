class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        maxi=0
        for i in range(len(s)):
            if s[i]=="E":
                c+=1
            else:
                c-=1
            maxi=max(maxi,c)
        return maxi