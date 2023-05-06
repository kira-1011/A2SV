class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        queue = deque(['0000'])
        visited = set(['0000'])
        turns = 0
        
        while queue:

            level_len = len(queue)

            for i in range(level_len):

                lock = queue.popleft()

                if lock in deadends:
                    continue

                if lock == target:
                    return turns

                for i in range(4):

                    digit = int(lock[i])

                    for direction in [1, -1]:
                        lock_new = str((digit + direction) % 10) 

                        new_lock = lock[ : i] + lock_new + lock[i + 1 : ]

                        if new_lock not in visited and new_lock not in deadends:
                            queue.append(new_lock)
                            visited.add(new_lock)

            turns += 1
        
        return -1
