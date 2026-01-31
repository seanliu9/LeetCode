#include <vector>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        if (n == 1)
        {
            return gas[0] >= cost[0] ? 0 : -1;
        }

        int total_surplus = 0; 
        int current_tank = 0; 
        int start_station = 0;

        for (int i = 0; i < n; i++) 
        {
            total_surplus += gas[i] - cost[i];
            current_tank += gas[i] - cost[i];

            // If we run out of gas at station i, then reset and start again at the next station
            if (current_tank < 0) 
            {
                start_station = i + 1;
                current_tank = 0;
            }
        }
        return total_surplus < 0 ? -1 : start_station;
    }
};