'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #DECLARE DICTIONARY VARIABLE
        #ESTABLISH A DICTIONARY THAT CORRELATES VAL:INDEX
        #CREATE A FOR LOOP TO ITERATE THE DICTIONARY... ON EACH ITERATION:
            #SUBTRACT CORRELATING KEY VALUE FROM TARGET VALUE
            #CHECK FOR EXISTENCE OF THE COMPLIMENT
            #RETURN THE KEY VALUE AS AN ARRAY ON A SUCCESS

        my_dict=dict()
        for index in range(len(nums)):
            my_dict[nums[index]] = index # adds KEY:VALUE (NUMS:INDEX)
        
        
        for i, value in enumerate(nums): 
            target2 = target - value
            if target2 in my_dict:
                if (my_dict[target2] == i):
                    pass
                else:
                    solution = [my_dict[target2],i]
                    return solution

