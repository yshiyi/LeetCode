class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)
        while left < right:
            mid = (right+left)//2
            if letters[mid]<=target:
                left = mid + 1
            else:
                right = mid
        return letters[left%len(letters)]
        
