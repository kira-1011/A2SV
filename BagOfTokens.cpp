class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
    
        int n = tokens.size(), p1 = 0, p2 = n - 1, score = 0, maxScore = 0;
        
        if(n == 1) maxScore = (power >= tokens[p1])? 1 : 0;
            
        sort(tokens.begin(), tokens.end());

        while(p1 <= p2)
        {
            if(power >= tokens[p1])
            {
                power -= tokens[p1];
                score++;
                p1++;
               
            }
            else if(power < tokens[p2] && score > 0)
            {
                power += tokens[p2];
                score--;
                p2--;
            }
            else if(power >= tokens[p2])
            {
                power -= tokens[p2];
                score++;
                p2--;
            }
            else
                p2--;
            
           if(maxScore < score) maxScore = score;

       
        }
        return maxScore;
    }
};