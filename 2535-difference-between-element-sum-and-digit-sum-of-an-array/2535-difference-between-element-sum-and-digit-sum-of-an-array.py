class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=sum(nums)
        Sum=0
        for i in nums:
            if i <10:
                Sum+=i
            else:
                while i >0:
                    digit=i%10
                    Sum+=digit
                    i=i//10
        return abs(element_sum-Sum)