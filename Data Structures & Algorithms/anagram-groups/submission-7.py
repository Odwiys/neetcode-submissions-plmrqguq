from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create result as a list
        # sort each s in strs (save as a key) and store them in answer (append to the same key)
        answer = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            answer[key].append(s)

        return list(answer.values())


        