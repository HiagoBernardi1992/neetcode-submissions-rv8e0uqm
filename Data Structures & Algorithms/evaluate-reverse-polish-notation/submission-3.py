class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for unit in tokens:
            if unit not in {'+', '-', '*', '/'}:
                stack.append(int(unit))
            else:
                right = stack.pop()
                left = stack.pop()

                match unit:
                    case '+':
                        stack.append(left + right)
                    case '-':
                        stack.append(left - right)
                    case '*':
                        stack.append(left * right)
                    case '/':
                        stack.append(int(left / right))

        return stack[0]
