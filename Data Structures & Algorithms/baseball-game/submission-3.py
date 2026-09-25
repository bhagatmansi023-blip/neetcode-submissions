class Solution:
    def calPoints(self, operations: List[str]) -> int:
        capacity = 1
        stack = [0] * capacity
        top = -1
       

        for op in operations:
            if top + 1 == capacity:
                capacity *= 2
                new_stack = [0] * capacity
                for i in range(top + 1):
                    new_stack[i] = stack[i]
                stack  = new_stack
            if op == '+':
                top += 1
                stack[top] = stack[top - 1] + stack[top - 2]
            elif op == 'C':
                top -= 1
            elif op == 'D':
                top += 1
                stack[top] = stack[top - 1] * 2
            else:
                top += 1
                stack[top] = int(op)
        total = 0
        for i in range(top + 1):
            total += stack[i]

        return total
                