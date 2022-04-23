class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int goodPairs = 0;
        
        for(int i = 0, n = nums.size(); i < n; i++){
            for(int j = i + 1; j < n; j++){
                if(nums[i] == nums[j])
                    goodPairs++;
            }
        }
        
        return goodPairs;
    }
    
};