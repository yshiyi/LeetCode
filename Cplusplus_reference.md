## C++ Reference
* [int vs unsigned int](#int-vs-unsigned-int)
* [Sorting Algorithm](#Sorting-Algorithm)

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





