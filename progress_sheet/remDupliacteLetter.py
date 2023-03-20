class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        visited = set()
        recent_index = defaultdict(int)
        mono_stack = []
        s_len = len(s)

        for i in range(s_len):
            recent_index[s[i]] = i

        for i in range(s_len):

            print(mono_stack)
        
            if s[i] in visited:
                continue
                
            while mono_stack and mono_stack[-1] >= s[i] and recent_index[mono_stack[-1]] > i:
                visited.remove(mono_stack.pop())

            mono_stack.append(s[i])
            visited.add(s[i])
        
        return ''.join(mono_stack)
