class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        # union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        # 1. union emails within same account
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        # 2. group emails by root
        groups = defaultdict(list)

        for email in email_to_name:
            root = uf.find(email)
            groups[root].append(email)

        # 3. build result
        res = []
        for root, emails in groups.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))

        return res
        