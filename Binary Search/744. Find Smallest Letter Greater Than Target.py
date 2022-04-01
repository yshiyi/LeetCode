class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1]<=target:
            return letters[0]
        left, right = 0, len(letters)
        while left < right:
            mid = (left+right)//2
            if letters[mid]<=target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
        
