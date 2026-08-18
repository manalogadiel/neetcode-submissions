class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if not s[i].isalnum():
                s = s.replace(s[i], " ")
        s = s.lower()
        s = "".join(s.split())
        
        return s[0:] == s[::-1]
        
        