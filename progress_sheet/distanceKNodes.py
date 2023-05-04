# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.target = None
        self.graph = None

    def bfs(self, root, k):

        queue = deque([root])
        visited = set([root])
        distance = 0

        # find nodes at distant k in the target node subtree
        while queue:

            if distance == k:
                return list(queue)

            level_len = len(queue)

            for i in range(level_len):

                node = queue.popleft()

                for next_node in self.graph[node]:

                    if next_node not in visited:
                        queue.append(next_node)
                        visited.add(next_node)

            distance += 1
        
        return []
    
    def constructGraph(self, root):

        if not root:
            return

        if root.left:
            self.graph[root.val].append(root.left.val)
            self.graph[root.left.val].append(root.val)

        if root.right:
            self.graph[root.val].append(root.right.val)
            self.graph[root.right.val].append(root.val)

        self.constructGraph(root.left)
        self.constructGraph(root.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)

        self.graph = graph
        
        # construct a graph
        self.constructGraph(root)

        # find the nodes at a distance k using BFS
        dist_k = self.bfs(target.val, k)
        
        return dist_k
