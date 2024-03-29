"""
752. Open the Lock

Description:
You have a lock in front of you with 4 circular wheels. 
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
 

Constraints:
1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

"""
Method: Use BFS.
        There are four wheels/digits that we can change each time.
        Check if it is one of the deadends. If it is, then just continue.
        Check if it has been visited. If it has, then continue.
        Then for each wheel, we turn it up and down, and insert the new string into the queue.
        这里，我们不能把visited.add() 放在for i in range(4)之前。因为这样效率会很低，每一个一加。
"""
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        step = 0
        q = collections.deque()
        q.append("0000")
        visited = set()
        visited.add("0000")
        while len(q):
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur==target:
                    return step
                if cur in deadends:
                    continue
                for i in range(4):
                    curUp = self.stepUp(cur, i)
                    if curUp not in visited:
                        q.append(curUp)
                        visited.add(curUp)
                    curDown = self.stepDown(cur, i)
                    if curDown not in visited:
                        q.append(curDown)
                        visited.add(curDown)
            step += 1
        return -1
    
    def stepUp(self, num, i):
        num = list(num)
        if num[i]=="9":
            num[i] = "0"
        else:
            num[i] = str(int(num[i])+1)
        return "".join(num)
    
    def stepDown(self, num, i):
        num = list(num)
        if num[i]=="0":
            num[i] = "9"
        else:
            num[i] = str(int(num[i])-1)
        return "".join(num)

       
"""
Method: Bidirectional BFS
        Notice, visited.add() excutes before for i in range(4).
        如果我们把每一个第一次见到的node就加进visited，比如在正向时获得target，把它加进visited。
        当反向时，因为target已在visited，就不能加进q。那在下一循环就不能检测是否相遇。
"""
def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited = set()
        q1 = collections.deque()
        q2 = collections.deque()
        q1.append('0000')
        q2.append(target)
        visited.add("0000")
        step = 0
        while len(q1) and len(q2):
            size = len(q1)
            for _ in range(size):
                seq = q1.popleft()
                if seq in deadends:
                    continue
                if seq in q2:
                    return step
                visited.add(seq)
                for i in range(4):
                    seq_up = self.up(seq, i)
                    seq_down = self.down(seq, i)
                    if seq_up not in visited:
                        q1.append(seq_up)
                        # visited.add(seq_up)
                    if seq_down not in visited:
                        q1.append(seq_down)
                        # visited.add(seq_down)
            step += 1
            q1, q2 = q2, q1
        return -1
