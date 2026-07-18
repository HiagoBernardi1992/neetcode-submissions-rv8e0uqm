class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for val in bills:
            if val == 5:
                five += 1
            if val == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            if val == 20:
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif ten == 0 and five >= 3:
                    five -= 3
                else: return False

        return True