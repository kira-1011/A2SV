class Solution {

public:
    int maxArea(vector<int>& height) {
        
        int maximumArea = 0;
        long long area = 0;
        
        int p1 = 0;
        int p2 = height.size() - 1;
        
        while(p1 != p2)
        {
            long long minHeight = min(height[p1], height[p2]);
            
            area = (p2 - p1) * minHeight;
            
            if(area > maximumArea)
                maximumArea = area;
            
            if(height[p1] > height[p2])
                p2--;
                
            else
                p1++;
        }
                
        return maximumArea;
    }
};