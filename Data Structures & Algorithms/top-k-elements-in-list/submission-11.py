class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Create the count
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Append to freq
        for key, value in count.items():
            freq[value].append(key)

        # check freq in desc order to append to res
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for x in freq[i]:
                res.append(x)
                if len(res) == k:
                    return res