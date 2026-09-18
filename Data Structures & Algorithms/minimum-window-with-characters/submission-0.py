class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
          return ""

        need = {}
        window = {}
        # Count characters needed from t
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = 0
        needCount = len(need)

        left = 0
        minLength = float("inf")
        result = [-1, -1]

        # Expand the window
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Character requirement satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Shrink the window while it is valid
            while have == needCount:

                # Update minimum window
                if (right - left + 1) < minLength:
                    minLength = right - left + 1
                    result = [left, right]

                # Remove left character
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = result
        return s[l:r + 1] if minLength != float("inf") else ""