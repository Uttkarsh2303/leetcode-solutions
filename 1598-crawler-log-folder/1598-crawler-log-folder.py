class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=[]
        for i in logs:
            if i =="../" and ans!=[]:
                ans.pop()
            elif i =="../" and ans==[]:
                continue
            elif i =="./":
                continue
            else:
                ans.append(i)
        return len(ans)