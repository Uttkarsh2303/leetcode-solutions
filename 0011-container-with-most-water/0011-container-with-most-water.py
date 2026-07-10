class Solution(object):
    def maxArea(self, height):
        left,right= 0,len(height)-1
        product = (right-left)*min(height[left],height[right])
        mx= product
        while left<right:
            if height[left]<height[right]:
                left+=1
            else:
             right-=1
            product = (right - left) * min(height[left], height[right])
            mx=max(product,mx)
        return mx

        