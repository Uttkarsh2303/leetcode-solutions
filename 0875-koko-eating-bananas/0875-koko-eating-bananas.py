class Solution(object):
    def minEatingSpeed(self, piles, h):
            def can_finish(k):
                hours_taken = 0
                for i in piles:
                    b = (i + k - 1) // k
                    hours_taken += b
                if hours_taken <= h:
                    return True
                return False
            low=1
            high=max(piles)
            while low<high:
                mid=low+(high-low)//2
                if can_finish(mid):
                    high=mid
                else:
                    low=mid+1
            return low
        