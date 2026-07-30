class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary_graph = {f: [] for f, _ in tickets }
        tickets.sort()
        for f, t in tickets:
            itinerary_graph[f].append(t)

        res = ["JFK"]
        def dfs(f):
            if len(res) == len(tickets) + 1:
                return True
            if f not in itinerary_graph:
                return False

            temp = list(itinerary_graph[f])
            for i, t in enumerate(temp):
                itinerary_graph[f].pop(i)
                res.append(t)

                if dfs(t):
                    return True

                itinerary_graph[f].insert(i, t)
                res.pop(t)
            return False

        dfs("JFK")
        return res

        