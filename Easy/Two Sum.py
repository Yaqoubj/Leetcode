class Solution(object):
 def twoSum(self, nums, target):
    #directly to store and serach faster    
     dic0 = {}
     # enumerate get both index and value 
     for i , num in enumerate(nums):
        diff = target - num
        #serach for the difference 
        if diff in dic0:
            #return index
            return [dic0[diff],i]
        # if false store index
        dic0[num] = i 
