'''
https://leetcode.com/problems/find-the-duplicate-number/description/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()
        for values in nums:
            if values in my_set:
                return values
            else:
                my_set.add(values) 
