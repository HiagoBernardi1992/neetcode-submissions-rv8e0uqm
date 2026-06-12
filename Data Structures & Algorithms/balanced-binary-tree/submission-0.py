# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return 0

            return max(1 + dfs(node.left), 1 + dfs(node.right))

        maxLeft = 0
        if root.left:
            maxLeft = 1 + dfs(root.left)

        maxRight = 0
        if root.right:
            maxRight = 1 + dfs(root.right)

        maxLeaf = max(maxLeft, maxRight)
        minLeaf = min(maxLeft, maxRight)
        diff = maxLeaf - minLeaf

        return False if diff > 1 else True
