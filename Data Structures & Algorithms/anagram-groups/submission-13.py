from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) # key (sorted): value (actual)

        for s in strs:
            key = "".join(sorted(s))
            group[key].append(s)

        return [val for val in group.values()]