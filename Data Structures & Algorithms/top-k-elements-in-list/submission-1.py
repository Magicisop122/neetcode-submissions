class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1

        heap = []

        for key, val in hashmap.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key])

            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]

        
        