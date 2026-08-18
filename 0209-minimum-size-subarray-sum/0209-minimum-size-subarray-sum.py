class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j= 0, 0
        window=0
        length=float('inf')
        min_len=length
        for j in range(len(nums)):
            window+=nums[j]
            length=j-i+1
            while window>=target:
                length = j - i + 1
                window-=nums[i]
                min_len = min(length, min_len)
                i+=1
            
        if min_len ==float('inf'):
            return 0
        return min_len