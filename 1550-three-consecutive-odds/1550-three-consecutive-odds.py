class Solution:
    def threeConsecutiveOdds(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                count+=1
            else:
                count=0
            if count==3:
                return True
        return False