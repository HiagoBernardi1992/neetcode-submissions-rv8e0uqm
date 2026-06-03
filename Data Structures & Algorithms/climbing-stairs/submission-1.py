class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        self.countStep = 0

        def recursion(step):
            if step > n:
                return
            if step == n:
                self.countStep += 1
            else:
                recursion(step + 1)
                recursion(step + 2)

        recursion(0)
        return self.countStep
