class Solution(object):
    def threeSum(self, nums):
        triplets=set()
        for i in range(len(nums)):
            target=-(nums[i])
            temp_nums=nums[i+1:]
            dict1={}
            for j,num in enumerate(temp_nums):
                diff = target-num
                if diff in dict1:
                    l1=[nums[i],num,diff]
                    l1.sort()
                    t=tuple(l1)
                    triplets.add(t)
                dict1[num]=j

        answer = [list(t) for t in triplets]
        return(answer)
        