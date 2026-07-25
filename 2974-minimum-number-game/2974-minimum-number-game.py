class Solution:
    def numberGame(self, arr: List[int]) -> List[int]:
        (arr.sort())
        i=0
        while i <len(arr):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            i+=2
        return arr