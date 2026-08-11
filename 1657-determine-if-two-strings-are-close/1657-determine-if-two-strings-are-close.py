class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        if sorted(set(word1))!=sorted(set(word2)):
            return False
        freq1={}
        for i in word1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        freq2={}
        for i in word2:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        list1=[]
        for values in freq1.values():
            list1.append(values)
        list1.sort()
        list2=[]
        for values in freq2.values():
            list2.append(values)
        list2.sort()
        if list1==list2:
            return True
        return False
        