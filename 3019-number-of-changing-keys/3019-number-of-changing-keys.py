class Solution:
    def countKeyChanges(self, s: str) -> int:
        q=s.lower()
        count=0
        for i in range(len(q)-1):
            if q[i]!=q[i+1]:
                count+=1
        return count