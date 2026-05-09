class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = {}

        # Count frequency
        for i in nums:
            h[i] = h.get(i, 0) + 1

        # Sort by frequency descending
        arr = sorted(h, key=h.get, reverse=True)

        return arr[:k]