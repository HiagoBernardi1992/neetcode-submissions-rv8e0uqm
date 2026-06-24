"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs(n, r, c):
            first = grid[r][c]
            allSame = True

            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != first:
                        allSame = False
                        break

                if not allSame:
                    break

            if allSame:
                return Node(first, True, None, None, None, None)

            half = n // 2

            topLeft = dfs(half, r, c)
            topRight = dfs(half, r, c + half)
            bottomLeft = dfs(half, r + half, c)
            bottomRight = dfs(half, r + half, c + half)

            return Node(
                True,
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return dfs(len(grid), 0, 0)
