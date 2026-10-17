class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {f: [] for f, _ in tickets}
        tickets.sort()
        for f, t in tickets:
            adj[f].append(t)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False

            temp = adj[src]
            for i, dst in enumerate(temp):
                adj[src].pop(i)
                res.append(dst)

                if dfs(dst): 
                    return True

                res.pop()
                adj[src].insert(i, dst)
            return False

        dfs("JFK")

        return res


        

        