class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        product=1
        while n>0:
            num=n%10
            product*=num
            sum+=num
            n=n//10
        return product-sum
        