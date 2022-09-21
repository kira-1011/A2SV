class Solution {
private:
    
    string repeat(string s, int n) {
        
        string repeat;

        for (int i = 0; i < n; i++)
            repeat += s;

        return repeat;
    }
    
    bool isNum(char num)
    {
        return (num >= 48 && num <= 57);
    }
    bool isLetter(char letter)
    {
        return (letter >= 97 && letter <= 122);
    }
public:
    string decodeString(string s) {
        
        string decoded = "";
        
        vector<string> stack;
        
        int n = s.length();
        
        for(int i = 0; i < n; i++)
        {
            
            if(s[i] != '[' && s[i] != ']')
            {
                if(isdigit(s[i]))
                {
                    string temp = "";
                    
                    while(isdigit(s[i]))
                    {
                        temp += s[i];
                        i++;
                    }
                    
                    stack.push_back(temp);
                }
                else
                {
                    string chr (1, s[i]);
                
                    stack.push_back(chr);
                    
                }
            }
            
            else if(s[i] == ']')
            {
                
                string temp = "";
                
                while(!isdigit(stack.back()[0]))
                {
                    temp = stack.back() + temp;
                    stack.pop_back();
                }
                
                temp = repeat(temp, stoi(stack.back()));
                
                stack.pop_back();
                
                stack.push_back(temp);
            }
        }
        
        while(!stack.empty())
        {
            decoded = stack.back() + decoded;
            stack.pop_back();
        }
        
        return decoded;
        
    }
};