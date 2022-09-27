class Solution {
private:
    
    //Minimax Algorithm
    
    int predictWinner(vector<int>& nums, int s, int e, int turn)
    {
        if(s >= e)
            return nums[s];
        
        int leftScore = predictWinner(nums, s + 1 , e , -1 * turn);
        
        int rightScore = predictWinner(nums, s , e - 1 , -1 * turn);
        
        leftScore += (turn * nums[s]);
        
        rightScore += (turn * nums[e]);
     
        return turn * max(turn * leftScore, turn * rightScore);
    }
    
public:
    bool PredictTheWinner(vector<int>& nums) {
        
        int score = predictWinner(nums, 0, nums.size() - 1, 1);
        
        return (score > -1);
    }
    
};