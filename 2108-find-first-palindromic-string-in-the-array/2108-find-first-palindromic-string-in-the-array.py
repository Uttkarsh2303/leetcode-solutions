class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_reverse(Str):
            i,j=0,len(Str)-1
            while i<=j:
                if Str[i]==Str[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        for i in words:
            if is_reverse(i):
                return i
        return ""