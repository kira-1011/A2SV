class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        
        vector<int>indices;
        
        int n = nums.size();
        sort(nums.begin(), nums.end()); //O(nlogn)
        
        for(int i = 0; i < n; i++){
                if(nums[i] == target)
                    indices.push_back(i);
        }
        
        return indices;
    }
};