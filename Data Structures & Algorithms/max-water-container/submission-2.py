class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        n=len(heights)
        r=n-1
        m = 0
        t = 0
        while l<r:
            t = min(heights[r],heights[l])* abs(r-l)
            m = max(t,m)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return m
