class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0] * len(s)
        pairs = {')':'(','}':'{',']':'['}
        top = -1

        for i in s:
            if i in pairs:
                if top != -1 and stack[top] == pairs[i]:
                    top -= 1
                else:
                    return False
            else:
                top += 1
                stack[top] = i
        return top == -1






