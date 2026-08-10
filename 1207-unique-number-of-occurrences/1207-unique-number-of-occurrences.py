class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        dict1={}
        for i,num in enumerate(arr):
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        occSet=set()
        for i in dict1.values():
            if i in occSet:
                return False
            occSet.add(i)
        return True