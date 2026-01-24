import java.util.Arrays;
import java.util.Comparator;
class Solution {
    public int findMinArrowShots(int[][] points) {
        int n = points.length;
        // Sort points by increasing order of start.
        Arrays.sort(points, new Comparator<int[]> () {
            @Override
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        int left = points[0][0];
        int right = points[0][1];
        int[] dp = new int[n];
        dp[0] = 1;
        for (int i = 1; i < n; i++)
        {
            if (points[i][0] <= right) // if the current arrow can burst the i-th balloon
            {
                dp[i] = dp[i - 1];
                left = points[i][0];
                right = Math.min(right, points[i][1]);
            }
            else // if the current arrow cannot burst the i-th balloon
            {
                dp[i] = dp[i - 1] + 1;
                left = points[i][0];
                right = points[i][1];
            }   
        }
        return dp[n - 1];
    }
}