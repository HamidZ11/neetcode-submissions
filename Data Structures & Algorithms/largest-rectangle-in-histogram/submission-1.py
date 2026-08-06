class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mystack = []
        maxArea = 0
        for index, height in enumerate(heights):
            start = index
            while mystack and height <= mystack[-1][1]:
                prev_start, h = mystack.pop()   
                start = prev_start
                width = index - start
                area = h * width
                maxArea = max(maxArea, area)

            mystack.append((start, height))

        while mystack:
            prev_start, h = mystack.pop()
            width = len(heights) - prev_start
            area = h * width
            maxArea = max(maxArea, area)

        return maxArea
