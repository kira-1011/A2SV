class Solution:

    def __init__(self):
        self.labels = None
        self.ans = []
        self.label_map = defaultdict(int)

    def dfs(self, tree, node, visited):

        descendants = [0] * 26
        visited.add(node)
        
        for next_node in tree[node]:
            
            if next_node not in visited:
                descendants1 = (self.dfs(tree, next_node, visited))
                descendants = [sum(i) for i in zip(descendants, descendants1)]  

        descendants[ord(self.labels[node]) - ord('a')] += 1

        self.ans[node] += descendants[ord(self.labels[node]) - ord('a')]

        return descendants

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        tree = defaultdict(list)
        self.labels = labels
        self.ans = [0] * n

        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        self.dfs(tree, 0, set())
        
        return self.ans
