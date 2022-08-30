class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
        int n = nums.size(), p1 = 0, p2 = n / 2;
        
        vector<int> rerearrangedArray;
        
        sort(nums.begin(), nums.end());
        
        
        while(p1 < (n / 2))
        {
            rerearrangedArray.push_back(nums[p2]);
            rerearrangedArray.push_back(nums[p1]);
            p1++;
            p2++; 
        }
        
        while(p2 < n)
        {
            rerearrangedArray.push_back(nums[p2]);
            p2++;
        }
        
        return rerearrangedArray;
    }
};