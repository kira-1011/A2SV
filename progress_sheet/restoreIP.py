class Solution:

    def __init__(self):
        self.s = ""
        self.solution = []

    def restoreIP(self, start_pos, dot_pos, address):

        if dot_pos == len(self.s):
            
            if len(address) == 4:
                self.solution.append('.'.join(address.copy()))

            return
        
        if len(address) == 4 and dot_pos < len(self.s):
            return
        
        segment = self.s[start_pos : dot_pos + 1]

        if segment[0] == '0' and len(segment) > 1:
            segment = '-1'

        if int(segment) >= 0 and int(segment) <= 255:

            address.append(segment)
            self.restoreIP(dot_pos + 1, dot_pos + 1, address)
            address.pop()
        
        self.restoreIP(start_pos, dot_pos + 1, address)


    def restoreIpAddresses(self, s: str) -> List[str]:

        self.s = s

        self.restoreIP(0, 0, [])

        return self.solution
