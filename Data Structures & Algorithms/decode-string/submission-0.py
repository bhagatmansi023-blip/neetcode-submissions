class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_number = 0

        for ch in s:
            if ch.isdigit():
                current_number = current_number * 10 + int(ch)

            elif ch == '[':
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0

            elif ch == ']':
                previous_string, repeat_count = stack.pop()
                current_string = previous_string + current_string * repeat_count

            else:
                current_string += ch

        return current_string