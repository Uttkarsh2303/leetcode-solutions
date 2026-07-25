class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        count = 0
        max_space = count
        for i in sentences:
            count = 0
            q="".join(i)
            for j in q:
                if j==" ":
                    count+=1

            count+=1
            max_space=max(max_space,count)
        return max_space