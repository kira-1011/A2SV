class Solution {

    
public:
    int minSetSize(vector<int>& arr) {
        
        int n = arr.size();
        
        vector<int> valFreq (*max_element(arr.begin(), arr.end()) + 1 , 0);
        
        int freqSum = 0;
        
        int setSize = 0;
        
        for(int i = 0; i < n; i++)
            valFreq[arr[i]]++;
        
        sort(valFreq.begin(), valFreq.end(), greater<int>());
        
        for(int i = 0; i < n; i++)
        {
            setSize++;
            
            freqSum += valFreq[i];
            
            if(freqSum >= (n / 2))
                break;
        }
        
        return setSize;
        
        
    }
};