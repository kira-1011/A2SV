class DataStream:

    def __init__(self, value: int, k: int):

        self.value = value
        self.k = k
        self.consecucitve = 0

    def consec(self, num: int) -> bool:

        if num != self.value:
            self.consecucitve = 0
            return False

        self.consecucitve += 1

        return  self.consecucitve >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
