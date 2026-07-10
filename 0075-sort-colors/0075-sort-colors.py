class Solution(object):
    def sortColors(self, nums):
        j=0
        l=len(nums)
        while (j<len(nums)):
            for i in range(l-1):
                if nums[i]>nums[i+1]:
                    nums[i+1],nums[i]=nums[i],nums[i+1]
            j+=1
            l-=1
        return nums
        