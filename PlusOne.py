class Solution:
    def plusOne(self, digits):
        b = ''.join(map(str,digits))
        c = int(b) + 1
        digit_list = [int(i) for i in str(c)]
        return list(digit_list)


obj = Solution()
print(obj.plusOne([4,3,2,1]))
