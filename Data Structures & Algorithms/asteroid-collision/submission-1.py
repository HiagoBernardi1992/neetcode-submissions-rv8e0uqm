class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    stack.pop()
                    asteroid = 0
            if asteroid != 0:
                stack.append(asteroid)
        return stack