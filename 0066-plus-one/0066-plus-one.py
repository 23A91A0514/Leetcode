class Solution:
    def plusOne(self, digits):
        l=[]
        s=0
        for i in digits:
            s=s*10+i
        s=s+1
        while(s>0):
            digit=s%10
            l.append(digit)
            s//=10
        return l[::-1]
