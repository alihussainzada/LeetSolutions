nums = [1,2,3,4]

class Solution:
    def containsDuplicate(self, nums):
        ls = set(nums)
        if len(nums) != len(ls):
            return True
        elif nums:
            return False
        else:
            return False
        
obj = Solution()
print(obj.containsDuplicate(nums))
