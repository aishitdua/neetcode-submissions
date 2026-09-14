class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        m = 1
        d = {}
        if n==0:
            return 0
        for i in range(n):
            if nums[i] in d.keys():
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        l = list(d.keys())
        l.sort()
        t=1
        for i in range(len(l)-1):
            if l[i+1]==l[i]+1:
                t+=1
            else:
                t=1
            m = max(m,t)
        return m