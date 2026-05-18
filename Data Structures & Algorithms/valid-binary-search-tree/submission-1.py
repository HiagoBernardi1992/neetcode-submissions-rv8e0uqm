# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, node: TreeNode, left: float, right: float):
        if not node:
            return True
            
        if not (node.val > left and node.val < right):
            return False
            
        return (self.isValid(node.left, left, node.val) and self.isValid(node.right, node.val, right))
    
            