class Solution:
    def reverseVowels(self, s: str) -> str:
        
        list1=list(s)
        vowels='aeiouAEIOU'
        list2=list(vowels)
        i,j=0,len(list1)-1
        while i <j:
            if list1[i] not in list2:
                i+=1
            elif list1[j] not in list2:
                j-=1
            else:
                list1[i], list1[j] = list1[j], list1[i]
                i += 1
                j -= 1
        q="".join(list1)
        return q
