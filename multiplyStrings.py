class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # Initialize all the needed variables
        len1 = len(num1)
        len2 = len(num2)
        integer1 = 0
        integer2 = 0
        product = 0

        # Convert num1 string to its equivalent integer
        for index in range(len1):
            integer1 += (int(num1[index]) * 10**(len1 - 1 - index))

        # Convert num2 string to its equivalent integer
        for index in range(len2):
            integer2 += (int(num2[index]) * 10**(len2 - 1 - index))
        
        # Final product of integer1 and integer2
        product = integer1 * integer2

        return str(product)