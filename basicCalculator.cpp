class Solution {
private:
     int evalRPN(vector<string> tokens ,unordered_map<string, int> &operators ) {
        
        vector<string> stackOps;
        
        stackOps.push_back(tokens[0]);
        
        int i = 1;
        
        while(i < tokens.size())
        {
            stackOps.push_back(tokens[i]);
            
            if(operators.find(tokens[i]) != operators.end())
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
    
    vector<string> toStringArray(string s, unordered_map<string, int> &operators)
    {
        vector<string> sArray;
        
        string temp = "";
        
        int n = s.length();
        
        for(int i = 0; i < n; i++)
        {
            string opChar;
            opChar.push_back(s[i]);
            
            if((int)s[i] == 32)
                continue;
            
            else if(operators.find(opChar) == operators.end())
                temp += opChar;
                
            
            else
            {
                sArray.push_back(temp);
                temp = "";
                temp = opChar;
                sArray.push_back(temp);
                temp = "";
            }
        }
        
        sArray.push_back(temp);
        
        return sArray;
    }
    
    vector<string> infixToPostfix(vector<string> sArray, unordered_map<string, int> &operators)
    {
        vector<string> stack;
        
        vector<string> RPN;
       
        for(int i = 0, n = sArray.size(); i < n; i++)
        {   
            if(operators.find(sArray[i]) == operators.end())
            {
                RPN.push_back(sArray[i]);
            }
            
            else
            {
                while(stack.size() != 0 && operators[sArray[i]] <= operators[stack.back()])
                {
                    RPN.push_back(stack.back());
                    stack.pop_back();
                }
                
                stack.push_back(sArray[i]);
           }
        }
        
        while(stack.size() != 0)
        {
            RPN.push_back(stack.back());
            stack.pop_back();
        }
        
        return RPN;
    }
    
public:
    int calculate(string s) {
        
        unordered_map<string, int> operators;
        
        operators["*"] = 1;
        operators["/"] = 1;
        operators["+"] = 0;
        operators["-"] = 0;
        
        vector<string> sArray = toStringArray(s, operators);
        
        vector<string> RPN = infixToPostfix(sArray, operators);
        
        return evalRPN(RPN,operators);
        
    }
};