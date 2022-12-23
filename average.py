class Solution:
    def average(self, salary: List[int]) -> float:
        
        # Initializing all the needed variables
        n = len(salary)
        total_sum = 0
        max_salary = 0
        min_salary = maxsize

        # Find min and max salary while taking the summation of the salaries
        for i in salary:
            max_salary = max(max_salary, i)
            min_salary = min(min_salary, i)
            total_sum += i

        # Take average of the salaries excluding the minimum and maximum salary
        average = (total_sum - max_salary - min_salary) / (n - 2)

        return average