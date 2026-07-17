class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l=[]
        for i in range(len(accounts)):
            s=0
            for j in range(len(accounts[i])):
                s+=accounts[i][j]
            l.append(s)
        return max(l)
        

        