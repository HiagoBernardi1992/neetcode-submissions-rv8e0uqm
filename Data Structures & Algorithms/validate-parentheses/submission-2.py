class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in "([{":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False

                bracket = stack.pop()

                if (
                    (b == ")" and bracket != "(")
                    or (b == "]" and bracket != "[")
                    or (b == "}" and bracket != "{")
                ):
                    return False

        return True if len(stack) == 0 else False
