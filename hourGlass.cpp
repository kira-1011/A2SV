class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        
        int m = grid.size(), n = grid[0].size(), maxSum = 0;
        
        //Prefix sum
        for(int i = 0; i < m; i++)
        {
            for(int j = 1; j < n; j++)
                grid[i][j] += grid[i][j - 1];
        }

        for(int i = 0; i < m - 2; i++){

            for(int j = 2, upSum = 0, midSum = 0, bottomSum = 0; j < n; j++){

                upSum = (j == 2)? grid[i][j] : grid[i][j] - grid[i][j - 3];
                midSum = grid[i + 1][j - 1] - grid[i + 1][j - 2];
                bottomSum = (j == 2)? grid[i + 2][j] : grid[i + 2][j] - grid[i + 2][j - 3];
                
                int sum = upSum + midSum + bottomSum;

                maxSum = max(maxSum, sum);
            }
        }

        return maxSum;
        
    }
};