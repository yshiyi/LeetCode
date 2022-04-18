"""
Sorted Iterator over K sorted lists

Description:
Given K sorted (ascending) arrays with N elements in each array, implement an iterator for iterating over the elements
of the arrays in ascending order.
The constructor receives all of the input as array of arrays.
You need to implement the MyIterator class with a constructor and the following methods.

class MyIterator<T>{
  T next();
  boolean hasNext();
}

You are allowed to use only O(K) extra space with this class.

Example:
input: [[1,5,7], [2,3,10], [4,6,9]]
The iterator should return: 1,2,3,4,5,6,7,9,10
"""
