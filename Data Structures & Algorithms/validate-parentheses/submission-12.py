class Solution:
    def isValid(self, s: str) -> bool:

        valid = ["()", "[]", "{}"]
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if not stack or stack.pop() + i not in valid:
                    return False
        
        return len(stack) == 0
                