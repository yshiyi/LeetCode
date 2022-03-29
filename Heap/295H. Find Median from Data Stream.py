'''
295. Find Median from Data Stream

Description:
The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''

# Solution:
'''
Method: Two heaps, one max_heap and one min_heap
        max_heap: has (n+1)/2 elements, the top of the heap is the maximum
        min_heap: has (n-1)/2 elements, the top of the heap is the minimum
        For example: [1,2,3,4,5,6,7]
        max_heap: [4,3,2,1]
        min_heap: [5,6,7]
        The median is either the top of max_heap or mean of tops of max and min heaps.
'''
class MedianFinder(object):

    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapq.heapify(self.max_h)
        heapq.heapify(self.min_h)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_h)==0 or num < -self.max_h[0]:
            heapq.heappush(self.max_h, -num)
        else:
            heapq.heappush(self.min_h, num)
        if len(self.max_h) > len(self.min_h)+1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
        elif len(self.min_h) > len(self.max_h):
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
        
    def findMedian(self):
        """
        :rtype: float
        """
        return -1.0*self.max_h[0] if len(self.max_h)>len(self.min_h) else (1.0*self.min_h[0] - 1.0*self.max_h[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
