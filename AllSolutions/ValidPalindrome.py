class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        non_alpha_chars = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/~` "  
        for i in non_alpha_chars:
            s = s.replace(i,"")
        
        if s == s[::-1]:
            return True
        else:
            return False
    
s = " "
obj = Solution()
print(obj.isPalindrome(s))
