# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def bfs(node, prev):
            if not node:
                return
            if node.val >= prev:
                self.count += 1
            prev = max(prev, node.val)
            bfs(node.left, prev)
            bfs(node.right, prev)

        bfs(root, float('-inf'))
        return self.count
        