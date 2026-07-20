class Solution(object):
    def mergeAlternately(self, word1, word2):
        list1=list(word1)
        list2=list(word2)
        list3=[]
        i,j=0,0

        while i < len(list1) and j<len(list2):
            list3+=list1[i]
            i+=1
            list3+=list2[j]
            j+=1
        if i <len(list1):
            list3+=list1[i:]
        if j <len(list2):
            list3+=list2[j:]
        word3=''
        for i in list3:
            word3+=i
        return word3