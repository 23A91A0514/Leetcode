# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        dum = root
        b = ""
        d = []
        def p(dum,d,b):
            if dum:
                b += str(dum.val)+"->"
                
                if not(dum.left) and not(dum.right):
                    d.append(b)
                      
                d = p(dum.left,d,b)
                d = p(dum.right,d,b)
            
            return d

        o = p(dum,d,b)

        for i in range(len(o)):
            o[i] = o[i][:len(o[i])-2]
        return o
        