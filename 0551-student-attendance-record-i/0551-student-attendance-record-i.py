class Solution:
    def checkRecord(self, s: str) -> bool:
        a=0
        y=1
        for i in range(len(s)-1):
            if(s[i]=="L" and s[i+1]=="L"):
                y+=1
            elif(y>=3):
                break
            else:
                y=1
        for i in range(len(s)):
            if(s[i]=="A"):
                a+=1
        if(a>=2 or y>=3):
            return False
        return True