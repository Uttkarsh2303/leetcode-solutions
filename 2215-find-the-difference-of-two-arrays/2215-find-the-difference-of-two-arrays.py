class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans0=set(nums2)
        ans1=set(nums1)
        list0=set()
        list1=set()
        for i in  nums1:
            if i not in ans0 and i not in list0:
                list0.add(i)
        for i in nums2:
            if i not in ans1 and i not in list1:
                list1.add(i)
        l0=list(list0)
        l1=list(list1)
        lAns=[l0,l1]
        return (lAns)