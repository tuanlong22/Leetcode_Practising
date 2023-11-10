class Solution(object):
    def singleNumber(self, nums):
        occur = defaultdict(int)
        for item in nums:
            if (item in occur):
                occur[item] += 1
            else:
                occur[item] = 1
        
        key_list = list(occur.keys())
        val_list = list(occur.values())

        position = val_list.index(1)
        return key_list[position] 
        
