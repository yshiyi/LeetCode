'''
Method 1:
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        ans.append(1)
        for i in range(1, rowIndex+1):
            ans.append(1)
            for j in range(i-1, 0, -1):
                ans[j] = ans[j] + ans[j-1]
        
        return ans
        
'''
Method 2: Recursive approach
'''
Pascal = defaultdict(list)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            Pascal[rowIndex] = [1]
            return [1]
        elif rowIndex == 1:
            Pascal[rowIndex] = [1, 1]
            return [1, 1]
        row = [0]*(rowIndex+1)
        row[0], row[-1] = 1, 1
        for i in range(1,len(row)-1,1):
            if rowIndex-1 not in Pascal:
                self.getRow(rowIndex-1)
            row[i] = Pascal[rowIndex-1][i-1] + Pascal[rowIndex-1][i]
        Pascal[rowIndex] = row
        return row
        
