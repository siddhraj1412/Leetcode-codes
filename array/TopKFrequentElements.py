class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = Counter(nums)

        # Step 2: Use heapq.nlargest to get top k frequent elements
        return heapq.nlargest(k, freq.keys(), key=freq.get)
