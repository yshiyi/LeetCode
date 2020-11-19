'''
599. Minimum Index Sum of Two Lists
Hash Table

Description:
Suppose Andy and Doris want to choose a restaurant for dinner, 
and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. 
If there is a choice tie between answers, output all of them with no order requirement. 
You could assume there always exists an answer.

Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
       list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
       list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Example 3:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
       list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 4:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
       list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 5:
Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]

Simliar Question:
Intersection of Two Linked Lists - Easy
'''

# Solution:
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        '''
        Method : At first, convert both lists to dictionary by using dict(zip(list, len(list)))
                 Loop through all the words in list1. 
                 If the word is also in list2, we then check if the summation of two values is less than min.
                 If so, we reset the result and save the word to result.
                 If the sum is equal to the min, we append the result.
        '''
        Dic1 = dict(zip(list1, range(len(list1))))
        Dic2 = dict(zip(list2, range(len(list2))))
        result = []
        index_ms = len(list1) + len(list2)
        for rest in Dic1:
            if rest in Dic2:
                if Dic1[rest] + Dic2[rest] < index_ms:
                    index_ms = Dic1[rest] + Dic2[rest]
                    result = []
                    result = [rest]
                elif Dic1[rest] + Dic2[rest] == index_ms:
                    result.append(rest)
        return result
