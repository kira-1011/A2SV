class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        candidates = []

        sources = set()
        destinations = set()

        for edge in edges:
            sources.add(edge[0])
            destinations.add(edge[1])
        
        for source in sources:
            if source not in destinations:
                candidates.append(source)
    
        return candidates
