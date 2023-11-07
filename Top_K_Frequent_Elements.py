class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        freq_count = defaultdict(int)
        
        # Count the frequency of each number
        for num in nums:
            freq_count[num] += 1
        
        # Sort the numbers by their frequencies in descending order
        sorted_freq = sorted(freq_count.keys(), key=lambda x: freq_count[x], reverse=True)
        
        # Get the top K frequent elements
        result = sorted_freq[:k]
        
        return result
