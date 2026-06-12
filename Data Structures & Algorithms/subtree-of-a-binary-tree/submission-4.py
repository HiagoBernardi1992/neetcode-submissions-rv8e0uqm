# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(treeOne: Optional[TreeNode], treeTwo: Optional[TreeNode]) -> bool:
            if not treeOne and not treeTwo:
                return True

            if not treeOne or not treeTwo or treeOne.val != treeTwo.val:
                return False

            return isSameTree(treeOne.left, treeTwo.left) and isSameTree(treeOne.right, treeTwo.right)

        if not subRoot:
            return True

        if not root:
            return False

        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        else: 
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            

        
        