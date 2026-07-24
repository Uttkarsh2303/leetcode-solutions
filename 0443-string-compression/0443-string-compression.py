class Solution:
    def compress(self, chars: List[str]) -> int:
        left=0
        right=0
        ans=""
        while right < len(chars):
            if right ==len(chars)-1:
                temp = chars[left:right + 1]
                l=(len(temp))
                print(l)
                if l==1:
                    ans+=chars[right]
                else:
                    l=str(l)
                    ans+=chars[right]
                    ans+=l
                right+=1
            elif chars[right+1]==chars[right]:
                right+=1
            else:
                temp=chars[left:right+1]
                l=(len(temp))

                if l==1:
                    ans+=chars[right]

                else:
                    l = str(l)
                    ans += chars[right]
                    ans+=l

                left=right+1
                right+=1
        for i in range(len(ans)):
            chars[i]=ans[i]
        return (len(ans))