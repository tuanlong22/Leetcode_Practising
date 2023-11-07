class Solution(object):
    def twoSum(self, numbers, target):
       l = 0
       r = len(numbers) - 1
       while(l<r):
           sum = numbers[l] + numbers[r]
           if(sum > target):
               r -= 1
           elif(sum<target):
               l += 1
           else:
               return[l+1,r+1]
        
