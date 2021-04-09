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
