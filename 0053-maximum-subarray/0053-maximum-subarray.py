class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        maxs=sum
        for i in range(1,len(nums)):
            sum+=nums[i]
            if nums[i]>sum:
                sum=nums[i]
            maxs=max(sum,maxs)

        return maxs