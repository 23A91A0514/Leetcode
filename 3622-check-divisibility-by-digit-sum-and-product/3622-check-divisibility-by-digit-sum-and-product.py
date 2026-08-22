class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        s = sum(int(d) for d in str(n))
        p=1
        while n>0:
            rev=n%10
            p*=rev
            n//=10
        total=s+p
        return temp%total==0 
        