# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        if not root:
            return self.good_nodes       

        def dfs(node, prev):
            if node.val >= prev:
                self.good_nodes += 1
                prev = node.val

            if node.left:
                dfs(node.left, prev)
            if node.right:
                dfs(node.right, prev)

        dfs(root, float('-inf'))
        return self.good_nodes 
        
        