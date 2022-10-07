class Solution {
public:
    int maxVowels(string s, int k) {
        
        unordered_map<char, int> vowels;
        
        vowels['a'] = 1;
        vowels['e'] = 1;
        vowels['i'] = 1;
        vowels['o'] = 1;
        vowels['u'] = 1;
        
        int n = s.length(), p1 = 0, p2 = 0, max = 0, countVowel = 0;
        
        while(p2 < k) 
        {
            if(vowels[s[p2]] > 0) countVowel++;
            
            if(countVowel > max) max = countVowel;
            
            p2++;
        }
        
        countVowel -= (vowels[s[p1]]);
        
        p1++;
        
        while(p2 < n)
        {   
            if(vowels[s[p2]] > 0) countVowel++;
            
            if(countVowel > max) max = countVowel;
            
            countVowel -= (vowels[s[p1]]);
            
            p1++;
            
            p2++;
        }
        
        return max;
    }
};