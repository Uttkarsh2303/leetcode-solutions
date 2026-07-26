class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product1 = 1
        product2=1

        for i in range(2):
            product1*=nums[i]
        product1*=nums[len(nums)-1]

        for i in range(len(nums) - 1, len(nums) - 4, -1):
                product2 *= nums[i]
        return max(product1,product2)