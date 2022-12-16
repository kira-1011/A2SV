class Solution {
public:
    bool isLetterOrDigit(char c){
        c = tolower(c);
        return (c >= 97 && c <= 122) || isdigit(c);
    }
    bool isPalindrome(string s) {
        int n = s.length(), p1 = 0, p2 = n - 1;

        while(p1 < p2)
        {
            while(p1 < n && !isLetterOrDigit(s[p1])) p1++;

            while(p2 >= 0 && !isLetterOrDigit(s[p2])) p2--;

            if((p1 >= n) || (p2 < 0)) return true;

            if(tolower(s[p1]) != tolower(s[p2])) return false;

            p1++;
            p2--;

        }

        return true;
    }
};