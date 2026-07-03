class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        n = len(cleaned)
        Len = int((n+1)/2)
        
        for i in range(Len):
            if cleaned[i] == cleaned[n-1-i]:
                continue
            else:
                return(False)
        
        return(True)