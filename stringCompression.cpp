class Solution {
public:
    int compress(vector<char>& chars) {
        
        string a = "";
        
        if(chars.size() == 1)
        {
            char x = chars[0];
            chars.clear();
            chars.push_back(x);
            return 1;
        }
        
        int p1 = 0, p2 = 1, n = chars.size(), c = 1;
        
        
        while(p2 < n)
        {
            if(chars[p1] == chars[p2])
            {
                c++;
                p2++;
            }
            else
            {
                a += chars[p1];
                if(c != 1)
                    a += to_string(c);
                p1 = p2;
                p2++;
                c = 1;
            }
        }
        
        a += chars[p1];
        if(c != 1)
            a += to_string(c);
        
        
        chars.clear();
        
        for(char s : a){
            chars.push_back(s);
        }
        return chars.size();
    }
};