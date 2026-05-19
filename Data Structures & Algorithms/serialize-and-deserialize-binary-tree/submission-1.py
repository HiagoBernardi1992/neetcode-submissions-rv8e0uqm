# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:       
        self.res = []
        self.dfsSerialize(root)
        return ",".join(self.res)
    
    def dfsSerialize(self, node: Optional[TreeNode]):
            if not node:
                self.res.append("N")
                return
            self.res.append(str(node.val))
            self.dfsSerialize(node.left)
            self.dfsSerialize(node.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.vals = data.split(",")
        self.index = 0
        return self.dfsDeserialize()

    def dfsDeserialize(self):
        if self.vals[self.index] == "N":
            self.index += 1
            return None
        node = TreeNode(int(self.vals[self.index]))
        self.index += 1
        node.left = self.dfsDeserialize()
        node.right  = self.dfsDeserialize()
        return node
            
