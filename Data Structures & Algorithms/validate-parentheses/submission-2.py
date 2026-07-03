class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for ch in s:
            if ch in pairs:
                #if ch is a closed pair
                if not stack or stack.pop() != pairs[ch]:
                    return(False)
            else:
                #if ch is a opened pair
                stack.append(ch)
        
        return not stack