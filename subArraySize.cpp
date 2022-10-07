class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        
        int p1 = 0, p2 = 0, n = arr.size(), sum = 0, subarray = 0;
        
        while(p2 < k)
        {
            sum += arr[p2];
            p2++;
        }
        
        if((sum / k) >= threshold) subarray++;
        
        sum -= arr[p1];
        
        p1++;
        
        while(p2 < n)
        {
            sum += arr[p2];
            
            if((sum / k) >= threshold) subarray++;
            
            sum -= arr[p1];
            
            p1++;
            
            p2++;
        }
        
        return subarray;
    }
};