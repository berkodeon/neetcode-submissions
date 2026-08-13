class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num]+= 1
            else:
                freq_map[num] = 1

        freq_list = [(freq, num) for num, freq in freq_map.items()]
        return [freq for _, freq in sorted(freq_list, reverse=True)][:k]