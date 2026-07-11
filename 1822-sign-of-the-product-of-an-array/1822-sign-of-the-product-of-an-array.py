class Solution(object):
    def arraySign(self, nums):
        negatives=0
        for num in nums:
            if num==0:
                return 0
            elif num<0:
                negatives+=1
        if negatives%2==0:
            return 1
        else:
            return -1
        