"""
621M. Task Scheduler
Description:
Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any order. 
Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period 
between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.
 
Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 
Constraints:
1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
Similar Questions:
Rearrange String k Distance Apart - Hard
Reorganize String - Medium
"""

"""
Method: Greedy
        For example, AAAABBBEEFFGG 3
        1. We need to first find the the letter which has the maximum frequency. In this case, it is A.
           And add n=3 spaces between each of them.
           A---A---A---A  (f_max-1)*n = 3*3 = 9
        2. Iteratively fill other letters in by the frequency
           AB--AB--AB--A  (fill in B)
           ABE-ABE-AB--A  (fill in E)
           ABEFABE-ABF-A  (fill in F)
           ABEFABEGABFGA  (fill in G)
        
        Notice: (f_max-1)*n returns the maximum space where we can fill in with other letters.
                If there exist another B which also appears 4 times, 
                we only need fill in 3 (min(f_max-1, f_B)) of them and put the last one to the end of string.
                e.g., AB--AB--AB--AB
                The task is to calculate the total number of idle that we need.
                In the end, we can simply add this number to the length of the original string.
        
        
        1. The maximum number of tasks is 26. 
           Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
        2. Iterate over the input array and store the frequency of task A at index 0, 
           the frequency of task B at index 1, etc.
        3. Sort the array and retrieve the maximum frequency f_max.
           This frequency defines the max possible idle time: idle_time = (f_max - 1) * n .
        4. Pick the elements in the descending order one by one. 
           At each step, decrease the idle time by min(f_max - 1, f) where f is a current frequency. 
           Remember, that idle_time is greater or equal to 0.
        5. Return busy slots + idle slots: len(tasks) + idle_time .
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n==0:
            return len(tasks)
        
        task_freq = collections.Counter(tasks)
        maxFreq = 0
        for task in task_freq.keys():
            if task_freq[task] > maxFreq:
                maxFreq = task_freq[task]
                maxTask = task
        
        idleTime = (maxFreq - 1) * n
        for task in task_freq.keys():
            if task!=maxTask:
                idleTime -= min(maxFreq-1, task_freq[task])
        """
        Consider this case:
        ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
        2
        idleTime will be negative.
        """
        idleTime = max(0, idleTime)
        return len(tasks)+idleTime
        

