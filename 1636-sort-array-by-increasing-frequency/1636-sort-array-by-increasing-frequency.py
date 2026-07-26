class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict1={}

        for i,num in enumerate(nums[::-1]):
            if num not in dict1:
                dict1[num]=1
            else:
                dict1[num]+=1
        sorted_dict = dict(sorted(dict1.items(), key=lambda x: (x[1],-x[0])))
        ans=[]
        for i,j in sorted_dict.items():
            for k in range(j):
                ans.append(i)

        return ans