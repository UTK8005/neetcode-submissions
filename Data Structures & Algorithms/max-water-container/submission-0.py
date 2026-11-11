class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep the item fixed,
        # traverse through the list the next pointer
        # set a max value 
        # calculate the product for the distance between the two
        # and the min of the two height bars
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
          min_height=min(heights[left],heights[right])
          distance=right-left
          area=min_height*distance
          if area>max_area:
            max_area=area
          if heights[left] <= heights[right]:
            left += 1
          else:
              right -= 1
        return max_area
        