class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {

        int n = cardPoints.size(), p1 = n - k, p2 = n - 1, score = 0, maxScore = 0;

        while(p1 < n)
        {
            score += cardPoints[p1];
            p1++;
        }
        
        p1 = n - k;
        
        while(p2 != k - 1)
        {
            if(maxScore < score) maxScore = score;

            score -=  cardPoints[p1];
            p1 = (++p1) % n;
            p2 = (++p2) % n;
            score +=  cardPoints[p2];
        }

        if(maxScore < score) maxScore = score;
        
        return maxScore;
    }
};