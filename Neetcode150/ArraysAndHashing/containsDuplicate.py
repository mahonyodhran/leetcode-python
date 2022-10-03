'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set(nums) # sets cannot have duplicates - so if there is a dupe, they won't be same length
        if(len(my_set) == len(nums)):
            return False
        return True

sol = Solution()

input = [1,2,3,1]
print(sol.containsDuplicate(input))

input = [1,2,3,4]
print(sol.containsDuplicate(input))