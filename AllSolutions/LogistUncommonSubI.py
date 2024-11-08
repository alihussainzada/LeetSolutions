class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if (a) == (b):
            return -1
        elif len(a) == len(b):
            return (len(a))
        elif len(a) != len(b):
            if len(a) > len(b):
                return (len(a))
            else:
                return (len(b))
       
a = "aefeaf"
b = "a"         
obj = Solution()
print(obj.findLUSlength(a,b))
