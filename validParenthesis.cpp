class Solution {
public:
    bool isValid(string s) {
        
        
        vector<char> stack;
        
        int i = 0;
        int n = s.length();
        
        if(n == 1)
            return false;
        
        stack.push_back(s[i]);
        
        
        
        while(i < n)
        {
            
            if(s[i] == ')' || s[i] == '}' || s[i] == ']')
            {
                char right =  stack.back();
                stack.pop_back();
                
                if(stack.size() == 0)
                    return false;
                
                char left =  stack.back();
                stack.pop_back();
                
                if(!((left == '{' && right == '}') || (left == '[' && right == ']') || (left == '(' && right == ')' ) ))
                    return false;
                
            }
             
            i++;
            
            if(i >= n)
                break;
            stack.push_back(s[i]);
          
        }
        
        if(stack.size() > 0)
            return false;
        
        return true;
    }
};