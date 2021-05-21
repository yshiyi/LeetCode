class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c=='+' or c=='-' or c=='*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for vl in left:
                    for vr in right:
                        if c=='+':
                            res.append(vl+vr)
                        elif c=='-':
                            res.append(vl-vr)
                        elif c=='*':
                            res.append(vl*vr)
            
        if len(res)==0:
            res.append(int(expression))
        return res
