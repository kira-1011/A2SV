class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = []
        size = len(boxes)

        for index1 in range(size):
            
            min_ops = 0

            for index2 in range(size):

                if boxes[index2] == '1':
                    min_ops += abs(index2 - index1)

            answer.append(min_ops)

        return answer