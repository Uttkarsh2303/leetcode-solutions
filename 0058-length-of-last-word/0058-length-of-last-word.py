class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)
        count=0
        j=len(s)-1
        while j>0:
            if s[j]==' ':
                j-=1
            else:
                break
        for i in range(j,-1,-1):
            if s[i]!=' ':
                count+=1
            if s[i]==' ':
                return count
        return count   