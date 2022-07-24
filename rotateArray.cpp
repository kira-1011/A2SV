class Solution {
private:
    void swap(int *x, int *y)
    {
        int temp = *x;
        *x = *y;
        *y = temp;
    }

public:
    void rotate(vector<int>& nums, int k) {
        
        int n = nums.size();
        
        if(n == 1)
            return;
        
        k = k % n;
        
        for(int p1 = n - k, p2 = n - 1; p1 < p2; p1++, p2--)
           swap(&nums[p1], &nums[p2]);
        
        
        for(int p1 = 0, p2 = n - k - 1; p1 < p2; p1++, p2--)
             swap(&nums[p1], &nums[p2]);
        
        
        for(int p1 = 0, p2 = n - 1; p1 < p2; p1++, p2--)
             swap(&nums[p1], &nums[p2]);
        
    }
};