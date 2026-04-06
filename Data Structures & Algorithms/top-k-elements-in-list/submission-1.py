class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item:item[1], reverse=True))

        result = list(sorted_frequency.keys())[:k]
        return result