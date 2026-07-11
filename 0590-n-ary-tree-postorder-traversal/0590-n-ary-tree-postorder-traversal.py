class Solution:
    def get_postorder(self, n, arr):
        if not n:
            return
        
        
        for child in n.children:
            self.get_postorder(child, arr)
        
        
        arr.append(n.val)
    
    
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        self.get_postorder(root, arr)
        return arr