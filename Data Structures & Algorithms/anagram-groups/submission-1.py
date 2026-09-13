from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            d["".join(sorted(i))].append(i)
        result = []
        for i in d.keys():
            result.append(d[i])
        return result
