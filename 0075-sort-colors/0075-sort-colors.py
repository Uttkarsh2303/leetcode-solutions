class Solution(object):
    def sortColors(self, nums):

        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1

            else:
                dict1[i]+=1


        sorted_dict=sorted(dict1.items())

        l=[]
        for a,b in sorted_dict:
            for i in range(b):
                l.append(a)
        nums[:]=l
        return nums



        