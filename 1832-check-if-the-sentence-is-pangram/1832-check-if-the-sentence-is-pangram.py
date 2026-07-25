class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        alphabets=[]
        for i in sentence:
            if i not in alphabets:
                alphabets.append(i)
        if len(alphabets)==26:
            return True
        else:
            return False