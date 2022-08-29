class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        
        int n = pushed.size(), p1 = 0, p2 = 0;
        
        vector<int> stack;
        
        
        while(p1 < n && p2 < n)
        {
            if(!stack.empty() &&( stack.back() == popped[p2]))
            {
                stack.pop_back();
                p2++;
            }
            else if(pushed[p1] == popped[p2])
            {
                p2++;
                p1++;
                
                if(p1 >= n)
                    p1--;
                
            }
            
            else
            {
                stack.push_back(pushed[p1]);
                p1++;
            }
        }
        
        return ((p2 < n)? false : true);
        
    }
};