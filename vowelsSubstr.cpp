class Solution {
public:
    long long countVowels(string word) {
        
        long long n = word.length();
        
        long long count = 0;
        
        unordered_map<char, int> vowels;
        
        vowels['a'] = 1;
        vowels['e'] = 1;
        vowels['i'] = 1;
        vowels['o'] = 1;
        vowels['u'] = 1;
        
        
        for(long long i = 0; i < n; i++)
        {
            if(i == 0 || i == n - 1)
            {
                if(vowels[word[i]] > 0)
                    count += n;
            }
            else if(vowels[word[i]] > 0)
                count += ((n + (i * (n - (i + 1)))));
        }
        
        return count;
    }
};