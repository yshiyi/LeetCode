"""
Description:
Given an int array wood representing the length of n pieces of wood and an int k. 
It is required to cut these pieces of wood such that more or equal to k pieces of the same length len are cut. 
What is the longest len you can get?

Example 1:
Input: wood = [5, 9, 7], k = 3
Output: 5
Explanation: 
5 -> 5
9 -> 5 + 4
7 -> 5 + 2

Example 2:
Input: wood = [5, 9, 7], k = 4
Output: 4
Explanation: 
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3

Example 3:
Input: wood = [1, 2, 3], k = 7
Output: 0
Explanation: We cannot make it.

Example 4:
Input: wood = [232, 124, 456], k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114 long, 
however we can't cut it into 7 pieces if any piece is 115 long.
"""

"""
Method: Binary Search
"""
def isValid(cutLen, arr, k):
  print(cutLen, arr, k)
  count = 0
  for wood in arr:
    if(wood >= cutLen):
      count += wood // cutLen
    else:
      return False
  print("Count:", count)
  if(count >= k):
    return True

def cutWood(arr, k):
  print(arr, k)
  left = 1
  right = max(arr)
  print("left-right:", left, right)
  res = 0
  while left < right:
    middle = (left + right) // 2
    if(isValid(middle, arr, k)):
      res = middle 
      left = middle + 1 
    else:
      right = middle  #

  return res 

wood = [232, 124, 456]
k = 7
print(cutWood(wood, k))
