class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n =len(nums)
        nums.sort()
        for i in range(n-2):
            target = -nums[i]
            l = i+1
            r = n-1
            while l<r:
                if nums[l] + nums[r] == target:
                    res.add(tuple([nums[i],nums[l],nums[r]]))
                    l+=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    r-=1
        return list(res)