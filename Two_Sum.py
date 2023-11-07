class Solution(object):
    def twoSum(self, nums, target):
        indices = {}
        res = []

        for i, a in enumerate(nums):
            if (target - a) in indices:
                res.append(indices[target - a])
                res.append(i)
                return res
            indices[a] = i
