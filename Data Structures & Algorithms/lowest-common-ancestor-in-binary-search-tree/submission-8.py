# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        minVal, maxVal = min(p.val, q.val), max(p.val, q.val)

        while root:
            if maxVal < root.val:
                root = root.left
            elif minVal > root.val:
                root = root.right
            else:
                return root
