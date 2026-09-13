class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for i in  range(len(nums))]
        suf = [1 for i in  range(len(nums))]
        pr = 1
        su = 1
        for i in range(len(nums)):
            pre[i] = pr
            pr *=nums[i]
        for i in range(len(nums)-1,-1,-1):
            suf[i] *= su
            su *=nums[i]
        res = [ pre[i]*suf[i] for i in range(len(nums))]
        return res