# This is a recursive solution
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [0] * (rowIndex+1)
        res[0] = 1
        if rowIndex==0:
            return res
        res[rowIndex] = 1
        preRow = self.getRow(rowIndex-1)
        for i in range(1, rowIndex):
            res[i] = preRow[i-1] + preRow[i]
        return res
