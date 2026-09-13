class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s={i: None for i in nums}
        for i in range(len(nums)):
            if s[nums[i]] is None:
                s[nums[i]]=1
            else:
                return True
        return False 