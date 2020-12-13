"""
347. Top K Frequent Elements
Hash Table, Heap

Description:
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:
Input: nums = [1], k = 1
Output: [1]

Similar Questions:
Word Frequency - Medium
Kth Largest Element in an Array - Medium
Sort Characters By Frequency - Medium
Split Array into Consecutive Subsequences - Medium
Top K Frequent Words - Medium
K Closest Points to Origin - Medium
"""

# Solution:
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        """
        Method 1: Create a dictionary to the hold the distinct element and its frequency, i.e., element: frequency.
                  Sort the dictionary.values(), and add the first k keys to the answer.
                  Remember to remove the key from the dictionary after the insertion.
        """
        Dic = {}
        ans = []
        for n in nums:
            Dic[n] = Dic.get(n, 0) + 1
        lst = Dic.values()
        lst.sort(reverse=True)
        for i in range(k):
            ans.append(Dic.keys()[Dic.values().index(lst[i])])
            del Dic[ans[i]]
        return ans
        
        
        """
        Method 2: Similar to Method 1.
                  Use collections.Counter to convert a list to a counter. 
                  A counter is a kind of dictionary in which the keys are the distinct elements and values are their frequencies.
                  Then use heapq.nlargest(n, iterable, key) to extract the n elements with most frequency.
                  heapq.nlargest(n, iterable, key) return a list with the n largest elements from the dataset defined by iterable. 
                  key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable.
                  In this case, key=count.get obtains the value of each element in count.keys() and find the largest n values.
                  
                  The property of this heap structure in Python is that each time the smallest of heap element is popped(min heap). 
                  Whenever elements are pushed or popped, heap structure in maintained. 
                  l = [5, 7, 9, 4, 3] 
                  # using heapify() to convert list into heap 
                  heapq.heapify(l)  # print(list(l)) -> [3, 4, 9, 5, 7]
                  # insert a value to heap
                  heapq.heappush(l, 10) # print(list(l)) -> [3, 4, 9, 5, 7, 10]
                  # pop the min value (which is 3) from heap
                  heapq.heappop(l)  # print(list(l)) -> [4, 5, 9, 10, 7]
                  # pop and return the smallest item from the heap, and also push the new item.
                  heapq.heapreplace(l, 2)  # print(list(l)) -> [2, 5, 9, 10, 7]
                  
        """
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
        
        
        
        """
        Method 3: Use quickselect, a.k.a. Hoare's selection algorithm.
                  Quickseelct is a textbook algorithm typicaly used to solve the problems "find kth something": 
                  kth smallest, kth largest, kth most frequent, kth less frequent, etc.
                  It has O(N) average time complexity, and its worst case time complexity is O(N^2).
                  Randomly select an element, and move less frequent elements to the left and others to the right.
        """
        # Count the frequency of each distinct element in nums
        count = Counter(nums)
        # Save the distinct elements in a list
        dis_nums = list(count.keys())

        # Define partition() to sort nums.
        # Elements with less frequency than pivot are moved to left, those with larger frequency are moved to right.
        def partition(left, right, pivot_index):
            pivot_freq = count[dis_nums[pivot_index]]
            # Move the pivot to the right
            dis_nums[pivot_index], dis_nums[right] = dis_nums[right], dis_nums[pivot_index]

            # store_index points to the position where the pivot will be moved to.
            # Specifically, it points to the position next to the elements with less frequency.
            store_index = left
            for i in range(left, right):
                if count[dis_nums[i]] < pivot_freq:
                    dis_nums[i], dis_nums[store_index] = dis_nums[store_index], dis_nums[i]
                    store_index += 1

            # Move pivot to position of store_index
            dis_nums[store_index], dis_nums[right] = dis_nums[right], dis_nums[store_index]
            return store_index
        
        # Define quickSelect() to find k smallest elements from
        # The reason to find the smallest is that k is always greater than 0
        def quickSelect(left, right, k_Smallest):
            # Check if there is only one element in nums
            if left == right:
                return

            # Randomly select a pivot in nums
            pivot_index = random.randint(left, right)
            # Sort nums
            index = partition(left, right, pivot_index)
            
            # if index == k_Smallest:
            #     return
            # # Go right
            # elif index < k_Smallest:
            #     quickSelect(index+1, right, k_Smallest)
            # # Go left
            # else:
            #     quickSelect(left, index-1, k_Smallest)
            
            while index != k_Smallest:
                if index < k_Smallest:
                    index = partition(index+1, right, random.randint(index+1, right))
                # Go left
                else:
                    index = partition(left, index-1, random.randint(left, index-1))
                print(index)
            return
         
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]
