class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        target_idx = 0
        
        for i in range(1, n + 1):
            if target_idx == len(target):
                break
                
            res.append("Push")
            
            if i == target[target_idx]:
                target_idx += 1
            else:
                res.append("Pop")
                
        return res