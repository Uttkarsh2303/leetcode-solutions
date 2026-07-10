class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i,num in enumerate(nums):
            diff=target-nums[i]
            if diff in dict:
                return i,dict[diff]
            dict[num]=i

        