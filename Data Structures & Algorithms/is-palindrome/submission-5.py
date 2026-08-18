class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if not s[i].isalnum():
                s = s.replace(s[i], " ")
        s = "".join(s.lower().split())
        
        return s == s[::-1]
        
        