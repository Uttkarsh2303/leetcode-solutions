class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum=sum(nums)
        lsum=0
        for i in range(len(nums)):
            rsum=rsum-nums[i]
            if rsum==lsum:
                return i
            lsum+=nums[i]
        return -1