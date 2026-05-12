class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            match bracket:
                case '(' |'{' |'[':
                    stack.append(bracket)
                case ')':
                    if not stack or  stack.pop() != '(':
                        return False
                case '}':
                    if not stack or  stack.pop() != '{':
                        return False
                case ']':
                    if not stack or  stack.pop() != '[':
                        return False
                case _:
                    return False
        
        if len(stack) > 0:
            return False
        else: 
            return True

        