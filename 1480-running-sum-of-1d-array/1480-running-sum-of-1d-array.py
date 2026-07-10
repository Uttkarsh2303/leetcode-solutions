class Solution(object):
    def runningSum(self, nums):
        ans=[nums[0]]
        for i in range(1,len(nums)):
            ans.append(nums[i]+ans[i-1])
        return ans