class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # handle edge case
        if not prerequisites:
            return True

        graph = defaultdict(list)
        incoming_edges = defaultdict(int)
        courses = []
        queue = deque()

        # build the graph of prerequisites
        for curr, pre in prerequisites:
            graph[pre].append(curr)
            incoming_edges[curr] += 1
        
        # find all the starting points
        for pre in range(numCourses):

            if incoming_edges[pre] == 0:
                queue.append(pre)

        # topological sorting using khans algorithm
        while queue:

            pre = queue.popleft()
            courses.append(pre)

            for next_pre in graph[pre]:

                incoming_edges[next_pre] -= 1

                if incoming_edges[next_pre] == 0:
                    queue.append(next_pre)

        return len(courses) == numCourses
