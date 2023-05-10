class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        available_tasks = []
        time = 0
        task_order = []
        tasks_len = len(tasks)

        for i in range(tasks_len):
            tasks[i].append(i)
        
        heapify(tasks)
        time = tasks[0][0]

        while len(task_order) != tasks_len:

            # find all the available tasks
            while tasks and tasks[0][0] <= time:
                eqt, pt, idx = heappop(tasks)
                heappush(available_tasks, (pt, idx))

            if available_tasks:
            
                # add the time of the task being processed
                curr_task = heappop(available_tasks)
                task_order.append(curr_task[-1])
                time += curr_task[0]
            
            else:
                time = tasks[0][0]

        return task_order
