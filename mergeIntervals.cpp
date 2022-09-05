class Solution {
private:
    static bool comparator(vector<int>& a, vector<int>& b)
    {
        return a[0] < b[0];
    }
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> merged;
        
        int n = intervals.size(), p1 = 0, p2 = 1;
        
        sort(intervals.begin(), intervals.end(), comparator);
        
        merged.push_back(intervals[0]);
        
        while(p2 < n)
        {
            
            if(merged[p1][1] >= intervals[p2][0])
               merged[p1][1] =  (merged[p1][1] > intervals[p2][1])? merged[p1][1] : intervals[p2][1];
               
            else
            {
                merged.push_back(intervals[p2]);
                p1++;
            }
            
            p2++;
        }
        
        return merged;
    }
};