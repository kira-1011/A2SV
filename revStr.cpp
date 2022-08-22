class Solution {

public:
    string reverseParentheses(string s) {
        
        
        vector<int> stack;
        
        int n = s.length();
        
        string res = "";
        
        for(int i = 0; i < n; i++)
        {
            if(s[i] == '(')
                 stack.push_back(res.length());
               
            else if(s[i] == ')')
            {
                int startIdx = stack.back();
                
                stack.pop_back();
                
                string subStr = res.substr(startIdx);
                
                reverse(subStr.begin(), subStr.end());
                
                res.replace(startIdx,subStr.length(),subStr);
            }
            else
                res += s[i];
        }
        
        return res;
        
    }
};