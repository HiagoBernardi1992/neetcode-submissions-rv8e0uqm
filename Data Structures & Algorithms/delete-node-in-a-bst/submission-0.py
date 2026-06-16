# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        curr = root
        while curr:
            if key > curr.val:
                curr = curr.right
            elif key < curr.val:
                curr = curr.left
            else:
                break

        if curr:
            if not curr.right and not curr.left:
                curr = None
            elif curr.right and not curr.left:
                curr.val = curr.right.val
                curr.right = None
            elif not curr.right and curr.left:
                curr.val = curr.left.val
                curr.left = None
            else:
                curr.val = curr.right.val
                curr.right = curr.left
                curr.left = None

        return root
