class Solution(object):
    def maxSubArray(self, nums):
        sum=nums[0]
        maxs=sum
        for i in range(1,len(nums)):
            sum=max(nums[i],nums[i]+sum)
            maxs=max(sum,maxs)

        return maxs
        