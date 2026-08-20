class StockSpanner:

    def __init__(self):
        self.stock = []
        

    def next(self, price: int) -> int:
        span = 0
        self.stock.append(price)
        for i in range(len(self.stock) - 1, -1, -1):
            if self.stock[i] <= price:
                span += 1
            else:
                break
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)