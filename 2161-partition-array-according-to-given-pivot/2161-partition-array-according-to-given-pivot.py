class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller_list=[]
        bigger_list=[]
        eq=[]
        for i in nums:
            if i>pivot:
                bigger_list.append(i)
            elif i==pivot:
                eq.append(i)
            else:
                smaller_list.append(i)
        return smaller_list+eq+bigger_list
                