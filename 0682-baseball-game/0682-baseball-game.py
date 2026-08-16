class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        index=0
        for i in range(len(operations)):
            if operations[i]=="D":
                ans.append(ans[index-1]*2)
                index+=1
            elif operations[i]=="C":
                ans.pop()
                index-=1
            elif operations[i]=="+":
                ans.append(ans[index-1]+ans[index-2])
                index+=1
            else:
                ans.append(int(operations[i]))
                index+=1
        return sum(ans)
            
            