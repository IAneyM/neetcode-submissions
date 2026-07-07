class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []
        for num, count in sorted_items[:k]:
            result.append(num)
        
        return(result)