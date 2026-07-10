class Solution(object):
    def addDigits(self, num):

        digit_sum=0
        while num>9:
            digit_sum = 0
            while num>0:
                digit_sum+=num%10
                num=num//10
            num=digit_sum

        return(num)
        