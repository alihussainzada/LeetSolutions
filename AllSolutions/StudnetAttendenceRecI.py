s = "LLLALL"

class Solution:
    def checkRecord(self, s: str) -> bool:
            if s.count("A") >= 2:
                return False
            counterL = 0
            for i in range(len(s)):
                if s[i] == "L":
                    counterL += 1
                    if counterL == 3:
                        return False
                else:
                    counterL = 0
            else:
                return True
        
obj = Solution()
print(obj.checkRecord(s))
