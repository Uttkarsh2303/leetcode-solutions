class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0=set(nums2)
        ans1=set(nums1)
        list0=[]
        list1=[]
        for i in  nums1:
            if i not in ans0 and i not in list0:
                list0.append(i)
        for i in nums2:
            if i not in ans1 and i not in list1:
                list1.append(i)
        listans=[list0,list1]
        return (listans)