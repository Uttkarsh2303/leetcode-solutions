class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n==0:
            return True
        i,j=0,0
        while i<n and j<m:
            if t[j]==s[i]:
                i+=1
            j+=1
            if i==n:
                return True
        return False