# Note: We must use deepcopy(path) to save it to self.res. Otherwise, the elements in self.res will be changed in accordance with the changes of path.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        self.traverse(graph, 0, path)
        return self.res
    
    def traverse(self, graph, s, path):
        path.append(s)
        if s==(len(graph)-1):
            self.res.append(deepcopy(path))
            path.pop()
            return
        for node in graph[s]:
            self.traverse(graph, node, path)
        path.pop()
