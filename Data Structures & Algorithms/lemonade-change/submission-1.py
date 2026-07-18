class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mine = 0
        for val in bills:
            if val > 5:
                give_back = val - 5
                mine -= give_back
                if mine < 0:
                    return False
                
            mine += val

        return True