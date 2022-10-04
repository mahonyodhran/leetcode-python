'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_set = set(nums)
        if(len(my_set) == len(nums)):
            return False
        return True

sol = Solution()

input = [1,2,3,1]
print(sol.containsDuplicate(input))

input = [1,2,3,4]
print(sol.containsDuplicate(input))