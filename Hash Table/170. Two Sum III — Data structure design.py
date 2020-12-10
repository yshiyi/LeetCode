'''
170. Two Sum III — Data structure design
Hash Table

Description:
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:
add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Example 2:
add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''


# Solution:
"""
Method: Create two sets.
        The first set contains all the elements that need to be added.
        The second set is used for function find. We sweep all the element in set1 and check if we have seen num - n.
        If not, we then save n to set2. If yes, return true.
"""

class TwoSum(object):
    def __init__(self):
        self.Set = set()

    def add(self, num):
        self.Set.add(num)

    def find(self, num):
        self.Set2 = set()
        for n in self.Set:
            if num - n not in self.Set2:
                self.Set2.add(n)
            else:
                return True
        return False


solution = TwoSum()
for i in [1, 3, 5]:
    solution.add(i)
print(solution.Set)

for num in [2, 4, 7, 8]:
    print(num, solution.find(num))





