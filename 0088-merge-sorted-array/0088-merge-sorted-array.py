class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j=0,0

        num1=nums1[:m]
        num2=nums2[:n]
        ans=[]
        while i<len(num1)and j<len(num2):
            if num1[i]<=num2[j]:
                ans.append(num1[i])
                i+=1

            else:
                ans.append(num2[j])
                j+=1


        while i<len(num1):
            ans.append(num1[i])
            i+=1

        while j<len(num2):
            ans.append(num2[j])
            j+=1
            
        nums1[:]=ans
        