class Solution:
    def smallestPalindrome(self, a: str) -> str:
        if len(a)<=1:
            return a
        s=sorted(a)
        dict1={}
        for i in s:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1

        middle=""
        for key in dict1.keys():
            if dict1[key]%2==1:
                middle+=key
                break



        for key in dict1.keys():
            dict1[key]//=2
        ans=''
        for key in dict1.keys():
            ans+=key*dict1[key]
        ansr="".join(reversed(ans))
        Ans=ans+middle+ansr
        return Ans