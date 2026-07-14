class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def getPattern(word, index):
            return word[:index] + "*" + word[index + 1:]

        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = getPattern(word, i)
                adj[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 0

        while q:
            res += 1
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = getPattern(word, j)
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                        adj[pattern] = []
        return 0    