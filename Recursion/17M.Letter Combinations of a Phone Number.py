class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return ""
        self.map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        temp = ""
        def backtrack(digits, temp, count):
            if count == len(digits):
                res.append(temp)
                return
            str = self.map[digits[count]]
            for i in range(len(str)):
                temp += str[i]
                backtrack(digits, temp, count+1)
                temp = temp[:-1]
        
        backtrack(digits, temp, 0)
        return res
