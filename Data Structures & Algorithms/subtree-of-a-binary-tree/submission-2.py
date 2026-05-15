# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
             return False
        if root.val == subRoot.val:
            if self.isSameTre(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTre(self, treeOne: Optional[TreeNode], treeTwo: Optional[TreeNode]) -> bool:
        if treeOne is None and treeTwo is None:
            return True
        elif treeOne is None or treeTwo is None or treeOne.val != treeTwo.val:
            return False
        else:
            return self.isSameTre(treeOne.left, treeTwo.left) and self.isSameTre(treeOne.right, treeTwo.right)
           
