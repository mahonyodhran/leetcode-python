'''
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''

def reverseString(s: list) -> list:
    """
    Do not return anything, modify s in-place instead. [Note: I return as a list just for my own testing - correct on Leetcode]
    """
    start = 0 # start index
    end = (len(s)-1) # last letter in list [0 indexed]

    while start <= end: #until they meet basically
        letter = s[start] # letter = first char in list [temp val]
        s[start] = s[end] # assign the current end letter to current start index
        s[end] = letter  # assign the temp value to the end - acts as a swap
        start += 1 # move up the list
        end -= 1 # move down the list

    return s