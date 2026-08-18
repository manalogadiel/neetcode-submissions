class Solution:
    def isPalindrome(self, s: str) -> bool:
        z = ''
        for i in s:
            if i.isalnum():
                z += i.lower()
        return z == z[::-1]
        
        