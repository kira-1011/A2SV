class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        
        int n = trips.size(), tripEnd = 0;

        for(int i = 0; i < n; i++)
            tripEnd = max(trips[i][2], tripEnd);

        tripEnd++;

        vector<int> totalPassengers(tripEnd, 0);

        for(int i = 0; i < n; i++)
        {
            totalPassengers[trips[i][1]] += trips[i][0];

            totalPassengers[trips[i][2]] -= trips[i][0];
        }

        for(int i = 1; i < tripEnd; i++)
        {
            totalPassengers[i] += totalPassengers[i - 1];

            if(totalPassengers[i] > capacity) return false;
        }

        if(totalPassengers[0] > capacity) return false;

        return true;
    }
};