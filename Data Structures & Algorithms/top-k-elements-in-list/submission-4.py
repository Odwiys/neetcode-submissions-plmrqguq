class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a counter from dict
        # create a freq counter from list
        # iterate through nums to add counts in nums
        # iterate through counter to add freq in freq
        # create a res list
        # iterate through freq in decreasing order (since our index now is also the count)
            # iterate freq in i and append freq to res
            # return if len(res) == k

        counter = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        for num, c in counter.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res