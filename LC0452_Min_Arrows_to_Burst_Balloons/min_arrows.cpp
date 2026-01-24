#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int n = points.size();
        // Sort points by increasing order of start.
        std::sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];  
        });

        int right = points[0][1];
        int dp [n];
        dp[0] = 1;
        for (int i = 1; i < n; i++)
        {
            if (points[i][0] <= right) // if the current arrow can burst the i-th balloon
            {
                dp[i] = dp[i - 1];
                right = std::min(right, points[i][1]);
            }
            else // if the current arrow cannot burst the i-th balloon
            {
                dp[i] = dp[i - 1] + 1;
                right = points[i][1];
            }
        }

        return dp[n - 1];
    }
};