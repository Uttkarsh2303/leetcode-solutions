class Solution(object):
    def trap(self, height):
        water=0


        max_left=height[0]
        left_list=[]
        for i in height:
            max_left=max(max_left,i)
            left_list.append(max_left)
        right_list=[]
        max_right=height[-1]
        for i in reversed(height):
            max_right=max(max_right,i)
            right_list.append(max_right)
        right_list.reverse()
        for i in range(len(height)):
            water+=min(left_list[i],right_list[i])-height[i]
        return water
        