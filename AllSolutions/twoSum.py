li = [2,5,5,11]
tar = 10

class Solution:
    def twoSum(self, nums,tar):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == tar:
                    return ([i,j])
                
obj = Solution()
print(obj.twoSum(li,tar))
