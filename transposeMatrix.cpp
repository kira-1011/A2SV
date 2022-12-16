class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        
        vector<vector<int>> transposeMatrix;

        int m = matrix.size(), n = matrix[0].size();

        for(int i = 0; i < n; i++){

            vector<int> columnVector;

            for(int j = 0; j < m; j++) columnVector.push_back(matrix[j][i]);

            transposeMatrix.push_back(columnVector);

        }

        return transposeMatrix;
    }
};