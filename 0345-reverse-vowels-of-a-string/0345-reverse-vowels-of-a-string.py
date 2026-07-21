class Solution(object):
    def reverseVowels(self, s):
        q=list(s)
        Vowels='aeiouAEIOU'
        vowels=list(Vowels)
        vs=[]
        for i in range(0,len(q)):
            if q[i] in vowels:
                vs.append(q[i])
                q[i]='_'
        vs.reverse()
        j=0
        for i in range(0,len(q)):
            if q[i]=='_':
                q[i]=vs[j]
                j+=1
        t=''.join(q)
        return t
        