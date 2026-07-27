class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_volume=0
        while i<j:
            smaller_height=min(height[i],height[j])
            volume=smaller_height*(j-i)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            max_volume=max(volume,max_volume)
        return max_volume
            