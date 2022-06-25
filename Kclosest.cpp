class Solution {

private:
    
    double euclideanDist(int x, int y){
          return (double)(sqrt((double)pow(x,2) + pow(y,2)));
    }
      
    static bool sortcol(vector<double>& v1, vector<double>& v2)
    {
         if(v1[0] >= v2[0])
            return false;
        
        return true;
    }
    
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        
        int n = points.size();
        
        vector<vector<double>> dist(n , vector<double> (2, 0));
        
        double distance = 0;
        
        vector<vector<int>> minPoints;
        
        for(int i = 0; i < n; i++){
            
            distance = euclideanDist(points[i][0], points[i][1]);
            
            dist[i][0] = distance;
            dist[i][1] = i;
            
        }
        
        sort(dist.begin(), dist.end(), sortcol);
        
        for(int i = 0; i < k; i++)
            minPoints.push_back(points[dist[i][1]]);
        
        return minPoints;
        
    }


};