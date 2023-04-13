class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        if len(roads) == 0:
            return 0

        graph = defaultdict(int)
        road_map = set()
        max_network = 0

        for road in roads:
            graph[road[0]] += 1
            graph[road[1]] += 1
            road_map.add(tuple(sorted(road)))
        
        for city1 in range(n):

            for city2 in range(city1 + 1, n):

                curr_network = graph[city1] + graph[city2]
            
                if tuple(sorted([city1, city2])) in road_map:
                    curr_network -= 1
            
                max_network = max(max_network, curr_network)

        return max_network
