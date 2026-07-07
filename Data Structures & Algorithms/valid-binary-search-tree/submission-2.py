# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node: Optional[TreeNode]):
            if not node.left and not node.right:
                return True
            if (node.left and node.left.val > node.val) or (node.right and node.right.val < node.val):
                return False
            else:
                return isValid(node.left) and isValid(node.right)

        return isValid(root)
            