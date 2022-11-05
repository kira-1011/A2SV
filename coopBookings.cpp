class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        
        int m = bookings.size();

        vector<int> totalSeats(n, 0);

        for(int i = 0; i < m; i++)
        {
            totalSeats[bookings[i][0] - 1] += bookings[i][2];

            if(bookings[i][1] < n) totalSeats[bookings[i][1]] -= bookings[i][2];
        }

        for(int i = 1; i < n; i++)
            totalSeats[i] += totalSeats[i - 1];

        return totalSeats;

    }
};