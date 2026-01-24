#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        
        // trivial case
        if (n == 1)
        {
            return citations[0] == 0 ? 0 : 1;
        }
        sort(citations.begin(), citations.end());
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
                temp = min(citations[i], n - i);
            }
            h_index = max(h_index, temp);
        }

        return h_index;
    }
};