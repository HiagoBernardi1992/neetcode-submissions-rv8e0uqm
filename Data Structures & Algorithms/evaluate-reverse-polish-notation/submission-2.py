class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        first = int(tokens[0])
        second = None
        for i in range(1, len(tokens)):
            if tokens[i] not in {'+', '-', '*', '/'}:
                second = int(tokens[i])
            else:
                match tokens[i]:
                    case '+':
                        first = first + second
                    case '-':
                        first = first - second
                    case '*':
                        first = first * second
                    case '/':
                        first = first / second
                    case _:
                        print("Invalid operator")
                second = 0

        return first
