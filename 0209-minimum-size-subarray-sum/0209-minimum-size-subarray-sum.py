class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=0
        window_sum=0
        min_len=float('inf')
        i=0
        for j in range(len(nums)):
            window_sum+=nums[j]
            length=j-i+1
            while i<len(nums) and window_sum>=target:
                window_sum-=nums[i]
                length=j-i+1
                i+=1
                min_len=min(min_len,length)
        if min_len==float('inf'):
            return 0
        return min_len