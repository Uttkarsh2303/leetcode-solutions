class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[0]*l
        left = [1] * l
        right = [1] * l
        n=0
        for i in nums:
            if i==0:
                n+=1

        p=1
        for i in nums:
            if i!=0:
                p*=i
        if n ==1:
            for i in range(len(nums)):
                if nums[i] ==0:
                    ans[i]=p
                else:
                    ans[i]=0

        elif n==0:

            for i in range(1,l):
                left[i]=left[i-1]*nums[i-1]
            for j in range(l-2,-1,-1):
                right[j]=right[j+1]*nums[j+1]
            for i in range(0,l):
                ans[i]=left[i]*right[i]

        return ans