## C++ Reference and Algorithms
* [int vs unsigned int](#int-vs-unsigned-int)
* [Sorting Algorithm](#Sorting-Algorithm)
* [Two Pointers](#Two-Pointers)
* [Sliding Window](#Sliding-Window)
* [Recursion](#Recursion)

# int vs unsigned int
A variable defined as int can be either positive or negative.\
A variable defined as unsigned int can only be non-negative.\
When comparing signed with unsigned, the compiler converts the signed value to unsigned.\
For example,
```
/* This works fine. 
   When an unsigned int decreases from 0 to 1, it will be automatically converted to 2^32-1.
   -1 is also converted to unsigned, i.e. (unsigned)-1
*/
for (unsigned int i = v.size()-1; i != -1; --i) 

/* This works fine.
   (unsigned)-1 is equal to 2^32 - 1
*/
for (unsigned int j = v.size()-1; j < (unsigned)-1; --j)

/* This doesn't work.
   Since (unsigned)-1 is equal to 2^32 - 1, i will never be greater than that value.
*/
for (unsigned int i = v.size()-1; i > -1; --i) 
```

# Sorting Algorithm
## 1. Bubble Sort
Bubble sort is the simplest technique in which we compare every element with its adjacent element and swap the elements if they are in wrong order (i.e., arr\[i\] > arr\[i+1\]). This way at the end of every iteration (called a pass), the heaviest element gets bubbled up at the end of the list.
```
C++
void bubbleSort(int * arr, int len) {
    for (int i=0; i<len-1; i++){
        for (int j=0; j<len-i-1; j++) {
            if (arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
```
```
Python
def BubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
```
### Recursive Bubble Sort
1. Base Case: If array size is 1, return.
2. Do One Pass of normal Bubble Sort. This pass fixes last element of current subarray.
3. Recur for all elements except last of current subarray.\
```
C++
void bubbleSort(int * arr, int len) {
    if (len == 1) {return;}
    for (int j=0; j<len-1; j++) {
         if (arr[j] > arr[j+1]){
             int temp = arr[j];
             arr[j] = arr[j+1];
             arr[j+1] = temp;
         }
     }
     bubbleSort(arr, len - 1);
}
```
```
Python
def RecurBubbleSort(nums, l):
    if l == 1:
        return nums
    for i in range(l-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    RecurBubbleSort(nums, l - 1)
```

## 2. Quick Sort

### Quickselect Algorithm
**[347M.Top K Frequent Elements](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/347M.%20Top%20K%20Frequent%20Elements.cpp)**\
Quickselect is a selection algorithm and is typically used to solve the problems "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent, etc. It is related to the quick sort sorting algorithm.\
The logic is simple, if index of partitioned element is more than k, then we recur for left part. If index is same as k, we have found the k-th smallest element and we return. If index is less than k, then we recur for right part.\
It has O(N) average time complexity and widely used in practice. It worth to note that its worth case time complexity is O(N^2), although the probability of this worst-case is negligible.
```
C++
class QuickSelect {
public:
    int quickSelect(vector<int>& nums, int left, int right, int k) {
        if (k>0 && k<= right-left+1) {
            int index = partition(nums, left, right);
            if (index - left == k-1) {
                return nums[index];
            }
            if (index - left > k - 1) {
                return quickSelect(nums, left, index - 1, k);
            }
            return quickSelect(nums, index+1, right, k-(index-left+1));
        }
        return -1;
    }

    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[right];
        int pivot_index = left;
        for (int i=left; i<right; i++) {
            if (nums[i] <= pivot) {
                swap(nums[i], nums[pivot_index]);
                pivot_index++;
            }
        }
        swap(nums[right], nums[pivot_index]);
        return pivot_index;
    }
};
```
```
Python
def partition(arr, l, r):
    pivot = arr[r];
    pivot_index = l;
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
    print(arr, pivot, pivot_index)
    return pivot_index

def quickSelect(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return quickSelect(arr, l, index-1, k)
        return quickSelect(arr, index+1, r, k-(index-l+1))
    return -1
```

# Two Pointers
There are two types of approaches using two pointers technique.
1. Fast and slow pointers\
   a. Two pointers run with different speed. If they tun on a straight path, the fast pointer will first arrive at the end eventually. If there is a circle, the fast pointer will catch up with the slow pointer.
   ```
   boolean hasCycle(ListNode head) {
       ListNode fast, slow;
       fast = slow = head;
       while (fast != null && fast.next != null) {
           fast = fast.next.next;
           slow = slow.next;

           if (fast == slow) return true;
       }
       return false;
   }
   ```
      Related question: 141. Linked List Cycle [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.py)\
   
   b. Using this technique, we can also determine the location of the starting node of the circle.\
      Related question: 142M. Linked List Cycle II [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/142M.%20Linked%20List%20Cycle%20II.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/142M.%20Linked%20List%20Cycle%20II.py)\
   
   c. Determine the middle node of a list.\
      Related questions: 876. Middle of the Linked List [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/876.%20Middle%20of%20the%20Linked%20List.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/876.%20Middle%20of%20the%20Linked%20List.py)\
   
   d. Determine the Nth node from the end of list.\
      Related questions: 19M. Remove Nth Node From End of List [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/19M.%20Remove%20Nth%20Node%20From%20End%20of%20List.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/19M.%20Remove%20Nth%20Node%20From%20End%20of%20List.py)

3. Left and right pointers\
   a. Binary search for a sorted array.
      ```
      int binarySearch(int[] nums, int target) {
       int left = 0; 
       int right = nums.length - 1;
       while(left <= right) {
           int mid = (right + left) / 2;
           if(nums[mid] == target)
               return mid; 
           else if (nums[mid] < target)
               left = mid + 1; 
           else if (nums[mid] > target)
               right = mid - 1;
       }
       return -1;
   }
      ```
    
   b. Two sums\
      Related question: 167. Two Sum II - Input array is sorted [C++](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.py)\
   c. Reverse an array\
      Related question: 344. Reverse String [C++](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.py)
   

# Sliding Window
Sliding window is a special method of two pointers. The basic idea is to use two different pointers to create a kind of window. Then, move this window by increasing the pointers individually. The time complexity is O(N). The basic logic is:
```
int left = 0, right = 0;
while (right < s.size()){
   window[s[right]]++;
   right++;
   
   while(window needs to shrink){
      window[s[left]]--;
      left--;
   }
}
```
**[76H. Minimum Window Substring](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/76H.%20Minimum%20Window%20Substring.cpp)**\
Description:\
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "". Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.\
Example 1:\
Input: s = "ADOBECODEBANC", t = "ABC"\
Output: "BANC"
```
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> window, need;
        for (auto& c:t) {
            need[c]++;
        }

        int left = 0, right = 0, match = 0;
        int start = 0, len = INT_MAX;
        while(right < s.size()) {
            char c = s[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                // if (window[c]==1){ This doesn't work, if there are duplicate char in target string.
                if (window[c]==need[c]){
                    match++;
                }
            }
            while (match == need.size()) {
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                char d = s[left];
                if (need.find(d)!=need.end()){
                    if (window[d]==need[d]){
                        match--;
                    }
                    window[d]--;
                }                
                left++;
            }
            right++;
        }
        
        if (len!=INT_MAX){
            string res = s.substr(start, len+1);
            return res;
        }else{
            return "";
        }
        
    }
};
```

# Recursion

700
509
98














