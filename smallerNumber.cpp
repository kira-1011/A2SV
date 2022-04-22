class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        
        int n = nums.size();
        vector<int>counts (n, 0);
        
        for(int i = 0, count = 0; i < n; i++){
            count = 0;
            for(int j = 0; j < n; j++){
                if(nums[j] < nums[i]){
                    count ++;
                    counts[i] = count;
                }
            }
        }
        
        return counts;
    }
};