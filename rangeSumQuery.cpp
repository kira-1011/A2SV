class NumMatrix {
private:
    
    vector<vector<int>> rowPrefixSum;
    
public:
    NumMatrix(vector<vector<int>>& matrix) {
        
        int rowN = matrix.size();
        int colN = matrix[0].size();
        
        vector<vector<int>> rowPrefixSum2 (rowN , vector<int> (colN, 0));
        
        rowPrefixSum = rowPrefixSum2;
        
        for(int i = 0; i < rowN; i++)
            rowPrefixSum[i][0] = matrix[i][0];
        
        for(int i = 0; i < rowN; i++ )
        {
            for(int j = 1; j < colN; j++)
                rowPrefixSum[i][j] = rowPrefixSum[i][j - 1] + matrix[i][j];
        }    
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        
        int rectRowN = row2 - row1 + 1;
        
        int sum = 0;
        
        for(int i = 0;  i < rectRowN; i++)
        {
            if(col1 == 0)
                sum += rowPrefixSum[row1 + i][col2];
            else
                sum += rowPrefixSum[row1 + i][col2] - rowPrefixSum[row1 + i][col1 - 1];
        }
        
        return sum;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */