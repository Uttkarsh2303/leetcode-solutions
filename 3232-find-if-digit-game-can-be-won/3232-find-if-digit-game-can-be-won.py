class Solution(object):
    def canAliceWin(self, nums):
        sum_single,sum_double=0,0
        for i in nums:
            if i<10:
                sum_single+=i
            else:
                sum_double+=i
        if sum_single==sum_double:
            return False
        else:
            return True
        