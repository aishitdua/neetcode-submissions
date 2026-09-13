class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        kd = sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]
        return [ i for i,j in kd ]