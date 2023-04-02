class Solution:

    def __init__(self):
        self.arr = []
        self.max_len = 0

    def findMaxLen(self, idx, s_list):

        if idx >= len(self.arr):
            return

        s = ''.join(s_list)
        set_s = set(s)
        set_arr = set(self.arr[idx])
        joint_set = set_s.intersection(set_arr)

        if len(joint_set) == 0 and len(set_arr) == len(self.arr[idx]):

            s_list.append(self.arr[idx])
            s = ''.join(s_list)
            self.max_len = max(self.max_len, len(s))
           
            self.findMaxLen(idx + 1, s_list)
            s_list.pop()
        
        self.findMaxLen(idx + 1, s_list)


    def maxLength(self, arr: List[str]) -> int:

        self.arr = arr

        self.findMaxLen(0, [])

        return self.max_len
