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
**Recursive Bubble Sort**
1. Base Case: If array size is 1, return.
2. Do One Pass of normal Bubble Sort. This pass fixes last element of current subarray.
3. Recur for all elements except last of current subarray.
```
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

**Recursive Bubble Sort**
fdsgdfsgsfdg
fgsdg
