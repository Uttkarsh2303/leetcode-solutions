class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3=''
        i,j=0,0

        while i < len(word1) and j<len(word2):
            word3+=word1[i]
            i+=1
            word3+=word2[j]
            j+=1
        if i <len(word1):
            word3+=word1[i:]
        if j <len(word2):
            word3+=word2[j:]
        return word3