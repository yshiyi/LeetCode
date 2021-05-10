class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        S = ""
        res = []
        left, right = 0, 0
        def backTracking(left, right, S):
            if len(S)==n*2:
                res.append(S)
                return
            else:
                if left < n:
                    backTracking(left+1, right, S+'(')
                if left > right:
                    backTracking(left, right+1, S+')')
                
                
        backTracking(left, right, S)
        return res
