class Solution:
    def numberGame(self, arr: List[int]) -> List[int]:
        nums=[0]*len(arr)
        (arr.sort())
        i=0
        while i <len(arr):
            nums[i],nums[i+1]=arr[i+1],arr[i]
            i+=2
        return nums