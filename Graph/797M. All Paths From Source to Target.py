# Note: We must use deepcopy(path) to save it to self.res. Otherwise, the elements in self.res will be changed in accordance with the changes of path.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.helper(graph, 0, path, res)
        return res
    
    def helper(self, graph, idx, path, res):
        path.append(idx)
        if idx==len(graph)-1:
            res.append(copy.deepcopy(path))
            return
        for node in graph[idx]:
            self.helper(graph, node, path, res)
            path.pop()
