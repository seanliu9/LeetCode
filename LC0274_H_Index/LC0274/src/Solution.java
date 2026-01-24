import java.util.Arrays;
class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        // trivial cases
        if (n == 1)
        {
            return citations[0] == 0 ? 0 : 1;
        }
        Arrays.sort(citations);
        int temp = 0;
        int h_index = 0;
        for (int i = 0; i < n; i++)
        {
            if (citations[i] == 0)
            {
                temp = 0;
            }
            else
            {
                temp = Math.min(citations[i], n - i);
            }
            h_index = Math.max(h_index, temp);
        }
        return h_index;
    }
}