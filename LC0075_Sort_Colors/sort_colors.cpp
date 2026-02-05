#include <vector>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        size_t n = nums.size();
        size_t count_0 = 0;
        size_t count_1 = 0;
        size_t count_2 = 0;
        for (size_t i = 0; i < n; i++)
        {
            if (nums[i] == 0)
            {
                count_0++;
            }
            else if (nums[i] == 1)
            {
                count_1++;
            }
            else
            {
                count_2++;
            }
        }

        for (size_t i = 0; i < count_0; i++)
        {
            nums[i] = 0;
        }
        size_t right_1_boundary = count_0 + count_1;
        for (size_t i = count_0; i < right_1_boundary; i++)
        {
            nums[i] = 1;
        }
        for (size_t i = right_1_boundary; i < n; i++)
        {
            nums[i] = 2;
        }
    }
};