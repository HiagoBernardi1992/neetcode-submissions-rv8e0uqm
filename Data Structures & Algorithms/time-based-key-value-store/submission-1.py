class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        arr = self.store[key]
        l, r = 0, len(arr) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2

            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

        
