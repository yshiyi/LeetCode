class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        st = collections.deque()
        heights.append(0)
        for i in range(len(heights)):
            # We can also use
            # st and heights[st[-1]] >= heights[i]
            # This is faster than len(st)
            while len(st) and heights[st[-1]] >= heights[i]:
                cur = st[-1]
                st.pop()
                if len(st)==0:
                    length = i
                else:
                    length = i - st[-1] - 1
                area = heights[cur] * length
                res = max(res, area)
            st.append(i)
        return res
