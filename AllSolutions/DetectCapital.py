class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True 
        elif word == word.lower():
            return True
        elif word == word[0].upper():
            return True
        elif word == word[0].upper() + word[1:].lower():
            return True
        else:
            return False

obj = Solution()
print(obj.detectCapitalUse("FlaG"))
word = "FlaG"
print(word == word[0].upper() + word[1:].lower())
print(word)
print(word[0].upper() + word[1:].lower())
