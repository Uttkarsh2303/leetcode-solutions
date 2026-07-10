class Solution(object):
    def maximumWealth(self, accounts):
        sum=0
        max_sum=sum
        for i in accounts:
            for j in i:
                sum+=j
            max_sum=max(sum,max_sum)
            sum=0
        return max_sum