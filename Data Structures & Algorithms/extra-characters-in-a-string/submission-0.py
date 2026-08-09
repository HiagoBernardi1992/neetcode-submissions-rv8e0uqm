class Trie:
    def __init__(self):
        self.children = {}
        self.end_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie()

        # Build Trie
        for word in dictionary:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = Trie()

                curr = curr.children[char]

            curr.end_word = True

        n = len(s)
        dp = [0] * (n + 1)

        # dp[n] = 0
        # Empty suffix has zero extra characters.

        for i in range(n - 1, -1, -1):
            # Option 1: s[i] is an extra character
            dp[i] = 1 + dp[i + 1]

            # Option 2: find dictionary words starting at i
            curr = root

            for j in range(i, n):
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]

                if curr.end_word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]
