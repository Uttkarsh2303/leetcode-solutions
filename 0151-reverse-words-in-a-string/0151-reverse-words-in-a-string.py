class Solution:
    def reverseWords(self, s: str) -> str:
        right = len(s) - 1
        ans = []
        while right>=0:
            while right >= 0 and s[right] == ' ':
                right-=1
            if right < 0:
                break
            left = right
            while left >= 0 and s[left]!=" ":
                left-=1
            word=s[left+1:right+1]
            ans.append(word)
            right=left-1

        return (" ".join(ans))