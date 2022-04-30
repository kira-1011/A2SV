class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int sumLeft = 0;
        int sumRight = 0;
        
        //8,4,1,2,5,7,2
        
        for (int i = 0, n = nums.size(); i < n; i++)
        {
            sumLeft = accumulate(nums.begin(), nums.begin() + i, 0);
            sumRight = accumulate(nums.begin() + i + 1, nums.end(), 0);

            if(sumLeft == sumRight)
                return i;
        }
        
        return -1;
    }
};