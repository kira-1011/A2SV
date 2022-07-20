class Solution {

private:
    
    string BS(int n)
    {
        if(n == 1)
            return "0";
        
        else
        {
            string s = BS(n - 1);
            return s + "1" + reverse(inverse(s));
        }
        
    }
    
    string reverse(string s)
    {
        string temp = "";
        
        for(int n = s.length(), i = n - 1; i >= 0; i--)
             temp += s[i];
        
        return temp;
    }
    
    string inverse(string s)
    {
        for(int i = 0, n = s.length(); i < n; i++)
            s[i] = (s[i] == '0')? '1' : '0';
        
        return s;
    }
        
    
public:
    char findKthBit(int n, int k) {
        string s = BS(n);
        
        return s[k - 1];
    }
};