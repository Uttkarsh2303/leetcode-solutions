class Solution(object):
    def sortedSquares(self, nums):
        ans=[0]*len(nums)
        i,j=0,len(nums)-1
        k=len(ans)-1
        while i<=j:
            left = nums[i] * nums[i]
            right = nums[j] * nums[j]
            if left>right:
                ans[k]=left
                i+=1

            else:
                ans[k]=right
                j-=1
            k-=1
        return(ans)
        