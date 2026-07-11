class Solution(object):
    def arraySign(self, nums):
        product=1
        for i in nums:
            product *= i
        print(product)
        if product>0:
            ans=1
        elif product<0:
            ans=-1
        else:
            ans=0  
        return ans
        