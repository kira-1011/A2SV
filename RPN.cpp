class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        vector<string> stackOps;
        
        vector<string> operators = {"*", "/" , "+" , "-" };
        
        stackOps.push_back(tokens[0]);
        
        int i = 1;
        
        while(i < tokens.size())
        {
            stackOps.push_back(tokens[i]);
            
            if(find(operators.begin(), operators.end(), tokens[i]) != operators.end())
            {
                stackOps.pop_back();
                        
                int rightOpr = stoi(stackOps.back());
                stackOps.pop_back();

                int leftOpr = stoi(stackOps.back());
                stackOps.pop_back();
                
                if(tokens[i] == "*")
                {
                    string res =  to_string(leftOpr * rightOpr);
                    stackOps.push_back(res);
                }
                else if(tokens[i] == "/")
                {
                    string res =  to_string(leftOpr / rightOpr);
                    stackOps.push_back(res);
                }
                else if(tokens[i] == "+")
                {
                    string res =  to_string(leftOpr + rightOpr);
                    stackOps.push_back(res);
                }
                else if(tokens[i] == "-")
                {
                    string res =  to_string(leftOpr - rightOpr);
                    stackOps.push_back(res);
                }
            }
            
            i++;
        }       
        
        return stoi(stackOps.back());
    }
};