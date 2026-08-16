class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1=[]
        for i in s:
            if i!="#":
                ans1.append(i)
            elif i=="#" and ans1!=[]:
                ans1.pop()
        ans2=[]
        for i in t:
            if i!="#":
                ans2.append(i)
            elif i=="#"and ans2!=[]:
                ans2.pop()
        return ans1==ans2