class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.makeTrie(words)

        ROWS = len(board)
        COLUMNS = len(board[0])

        res = set()
        visited = set()

        def dfs(r, c, node, word):

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLUMNS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            letter = board[r][c]
            node = node.children[letter]

            word += letter

            if node.endOfWord:
                res.add(word)

            visited.add((r, c))

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r, c, root, "")

        return list(res)

    def makeTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()

        for word in words:
            cur = root

            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()

                cur = cur.children[letter]

            cur.endOfWord = True

        return root