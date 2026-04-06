from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            answer = defaultdict(list)

            for s in strs:
                key = ''.join(sorted(s))
                answer[key].append(s)

            return list(answer.values())

        # import defaultdict from collections
        # create answer with defaultdict
        # iterate through strs
            # sort the word in str (gives you a list), join them back as a string
            # append string to answer
        # return answer

