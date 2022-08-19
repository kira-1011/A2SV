class Solution {
public:
    bool isValid(string s) {
        
        int n = s.length();
        
        unordered_map<char, char> bracketPairs;
        vector<int> stack;
        
        bracketPairs[')'] = '(';
        bracketPairs[']'] = '[';
        bracketPairs['}'] = '{';
        
        
        for(int i = 0; i < n; i++)
        {
            if(bracketPairs[s[i]] != '\0')
            {
                if(!stack.empty() && bracketPairs[s[i]] == stack.back())
                    stack.pop_back();
                
                else
                    return false;
            }
            else
                stack.push_back(s[i]);
        }
        
        return (stack.empty());
    }
};