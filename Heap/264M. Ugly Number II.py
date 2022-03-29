'''
264. Ugly Number II

Description:
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:
1 <= n <= 1690
'''

# Solution:
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        primes = [2, 3, 5]
        q = [1]
        heapq.heapify(q)

        count = 0
        while count < n:
            ans = heapq.heappop(q)
            while len(q)>0 and ans==q[0]:
                heapq.heappop(q)
            count += 1
            for prime in primes:
                heapq.heappush(q, prime*ans)
                if ans%prime==0:
                    break
        return ans
        
