class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        
        sort(nums.begin(),nums.end(), compare);

        return nums[k - 1];
        
    }

private:
    
    static bool compare(string a, string b)
    {

        if(a.length() > b.length())
            return true;

        if(a.length() == b.length())
            return a > b;

        return false;
    }
};