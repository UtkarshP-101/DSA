class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        area=[]
        while left < right:
            if height[left]>height[right]:
                area.append((-left+right)*height[right])
                right -= 1
            else:
                area.append((-left+right)*height[left])
                left +=1
        return max(area)
        