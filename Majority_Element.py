class Solution(object):
    def majorityElement(self, nums):
        occur = {}
        for i in nums:
            if i in occur:
                occur[i] += 1
            else:
                occur[i] = 1    
        key_list = list(occur.keys())
        val_list = list(occur.values())
        position = val_list.index(max(val_list))
        return key_list[position]
        
