class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        elif n==1:
            return True
        if n%10!=4 and n%10!=6:
            return False
        elif n%2!=0:
            return False
        else:
            return self.isPowerOfFour(n/4)