class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        tem=num
        while(num>0):
            digit=num%10
            if tem%digit==0:
                c+=1
            num//=10
        return c
        