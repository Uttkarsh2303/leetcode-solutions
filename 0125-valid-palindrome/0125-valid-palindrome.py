class Solution(object):
    def isPalindrome(self, s):
        import string
        a= s.lower()
        pc = string.punctuation+" "
        b=""
        for i in a:
            if i not in pc:
                b+=i
        
        left,right=0,len(b)-1

        while left<right:
            if b[left]!=b[right]:
                return False
            left+=1
            right-=1

        return True

        