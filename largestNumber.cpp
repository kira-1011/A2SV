class Solution {
private:
    static bool comp(string& s1, string& s2)
    {   
        int n = s1.length(), m = s2.length(), i = 1, j = 1;
        
        if(n != m)
            return ((s1 + s2) > (s2 + s1));
        
        char a = s1[0];
        char b = s2[0];
        
        while(a == b && (i < n || j < m))
        {
            
            if(i < n)
            {
                a = s1[i];
                i++;
            }
                
            if(j < m)
            {
                b = s2[j];
                j++;
            }
        }
        
        return a > b;
    }
    
public:
    string largestNumber(vector<int>& nums) {
        
        vector<string> stringNums;
        
        int n = nums.size();
        
        string res = "";
        
        for(int i = 0; i < n; i++)
            stringNums.push_back(to_string(nums[i]));
        
        sort(stringNums.begin(), stringNums.end(), comp);
        
        if(stringNums[0] == "0")
            return "0";
        
        for(auto i : stringNums)
            res += i;
        
        return res;
    }
};