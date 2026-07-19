class Solution(object):
    def scoreOfString(self, s):
        q=[]
        score=0
        for i in s:
            q.append(ord(i))



        for i in range(len(q)-1) :
            abs_val=abs(q[i]-(q[i+1]))
            score+=abs_val

        return score
        