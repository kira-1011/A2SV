class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        
        int n = nums.size(), currentK = k, p1 = 0, p2 = 1, max = 1;
        
        sort(nums.begin(), nums.end());
        
        while(p2 < n)
        {
            long int diff = nums[p2] - nums[p2 - 1];
            
            long int needed = diff * (p2 - p1);
            
            while(p1 < p2 && needed > currentK)
            {
                currentK += (nums[p2 - 1] - nums[p1]);
                p1++;
                needed = diff * (p2 - p1);
            }
            
            currentK -= needed;
            
            if(max < (p2 - p1 + 1)) max = (p2 - p1 + 1);
            
            p2++;
        }
        
        return max;
        
    }
}; 
