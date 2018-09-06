from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        nodes = self.getAllNodes(node)
        node_map = {}
                
        for orig_node in nodes:
            node_map[orig_node] = UndirectedGraphNode(orig_node.label)

        for orig_node in node_map:
            for orig_neighbor in orig_node.neighbors:
                node_map[orig_node].neighbors.append(node_map[orig_neighbor])

        return node_map[node]

    def getAllNodes(self, root):
        queue = deque([root])
        ret = []
        while queue:
            node = queue.popleft()

            if not node:
                continue
            
            ret.append(node)
            for neighbor in node.neighbors:
                if neighbor not in ret:
                    queue.append(neighbor)

        return ret

