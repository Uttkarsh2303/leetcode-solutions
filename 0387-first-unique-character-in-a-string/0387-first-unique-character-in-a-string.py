class Solution(object):
    def firstUniqChar(self, s):
        l=list(s)
        dict1={}
        target=-1

        for i in (l):
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1




        for ch in s:
            if dict1[ch]==1:
                element=ch
                return (s.index(element))
        

        return target
        