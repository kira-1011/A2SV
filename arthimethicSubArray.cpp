class Solution {
    
private:
    vector<int> subArray;
    
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        
        int m = l.size();
        
        int d = 0;
        
        bool ans = true;
        
        vector<bool> answer;
        
        for(int i = 0; i < m; i++)
        {
            ans = true;
            
            copy(nums.begin() + l[i], nums.begin() + r[i] + 1, back_inserter(subArray));
            
            sort(subArray.begin(), subArray.end());
            
            d = subArray[1] - subArray[0];
            
            for(int j = 0, n = r[i] - l[i], diff = 0; j < n; j++){
                
                diff = subArray[j+1] - subArray[j];
                
                if(diff != d)
                {
                    ans = false;
                    break;
                }
                    
            }
            
            answer.push_back(ans);
            
            subArray.clear();
        }
        
        return answer;
    }
};


    