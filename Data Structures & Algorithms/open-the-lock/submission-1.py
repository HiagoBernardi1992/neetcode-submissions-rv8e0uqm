def openLock(self, deadends: List[str], target: str) -> int:
        # If the starting point is blocked, it's impossible to proceed
        if "0000" in deadends:
            return -1
            
        def get_neighbors(lock):
            res = []
            for i in range(4):
                # Turning the wheel up (+1)
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                # Turning the wheel down (-1)
                digit = str((int(lock[i]) - 1) % 10) # Python handles negative modulo smoothly
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque([("0000", 0)])
        
        visited = set(deadends)
        visited.add("0000")
        
        while q:
            lock, turns = q.popleft()
            
            if lock == target:
                return turns
            
            for neighbor in get_neighbors(lock):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, turns + 1))

        return -1