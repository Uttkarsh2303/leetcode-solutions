class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict1={}
        count=0
        for num in nums:
            diff=k-num
            if diff in dict1:
                if dict1[diff]==1:
                    del dict1[diff]
                else:
                    dict1[diff]-=1
                count+=1
            else:
                if num in dict1:
                    dict1[num]+=1
                else:
                    dict1[num]=1
        return count