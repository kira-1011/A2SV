class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        int count = 0;
        int kth = 0;
        
        make_heap(nums.begin(), nums.end());
        
        while(count < k)
        {
            kth = nums.front();
            pop_heap(nums.begin(), nums.end());
            nums.pop_back();
            count++;
        }
                           
        return kth;
        
    }
};