"""
380. Insert Delete GetRandom O(1)
Array, Hash Table, Design

Description:
Implement the RandomizedSet class:
1. bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
2. bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
3. int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
   Each element must have the same probability of being returned.
Follow up: Could you implement the functions of the class with each function works in average O(1) time?

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Similar Question:
Insert Delete GetRandom O(1) - Duplicates allowed - Hard
"""

# Solution:
"""
Method: To insert or remove a value, we need to use hash table which takes O(1) operation time.
        To randomly select a value, we need to use array which takes O(1) operation time. Hash table doesn't support such function.
        Therefore, we need to create a array to save the unique values. 
        We also need to create a dictionary in which the key is the unique value and the value is the index of that value in the array.
        
        To insert a value, if the value is not in the dictionary, we first save the value to the array.
        And we save the value and the current length of the array in the dictionary. The current length of the array represents the index.
        
        As to remove a value, if we remove a value from the dictionary, the index will not be consistent.
        In order to address this problem, we swap the last value and the target value in the dictionary and remove the last one.
        We first determine the last value in the array, nums[-1], and find out the index of the target value, Dic[val].
        We then swap the last value and the target value in nums, nums[-1], nums[Dic[val]] = nums[Dic[val]], nums[-1].
        Change the index of the last one in dictionary, Dic[nums[-1]] = Dic[val].
        Finally, remove the last value from the array and remove the key [val] from the dictionary.
        
        To randomly select a value, we only need to randomly select one from the array nums using random.choice(nums).
        This takes O(1) operation time.
        
"""
from random import choice

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = [] # Space O(N)
        self.hashTable = {} # Space O(N)

    def insert(self, val): # Time O(1)
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not val in self.hashTable:
            self.nums.append(val)
            self.hashTable[val] = len(self.nums) - 1
            return True
        else:
            return False

    def remove(self, val): # Time O(1)
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.hashTable:
            return False
        else:
            lastNum = self.nums[-1]
            valIndex = self.hashTable[val]
            if lastNum != val:
                #Swap
                self.nums[-1], self.nums[valIndex] = self.nums[valIndex], self.nums[-1]
                self.hashTable[lastNum] = valIndex
            # It means that always delete val at the last of nums list
            self.nums.pop(-1)
            del self.hashTable[val]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return choice(self.nums) # Time O(1)
