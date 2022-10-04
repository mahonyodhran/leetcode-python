'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 2:
            return [0,1] 

        mappy = {}
        for index, number in enumerate(nums):
            goal = target - number # we know we need to find a certain number
            if goal in mappy: # if that goal number is already in the hashmap, enter this block and return
                return[mappy[goal], index]
            mappy[number] = index

sol = Solution()

nums = [2,7,11,15] 
target = 9
print(sol.twoSum(nums, target))
# Output: [0,1]

nums = [3,2,4]
target = 6
print(sol.twoSum(nums, target))
# Output: [1,2]

nums = [3,3] 
target = 6
print(sol.twoSum(nums, target))
# Output: [0,1]