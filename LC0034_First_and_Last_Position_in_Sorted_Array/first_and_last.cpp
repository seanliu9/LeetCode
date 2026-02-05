#include <vector>
using namespace std;

class Solution {
public:
    int rSearchRange(const vector<int>& nums, const int target, const int left, const int right, const bool find_first) const
    {
        if (left > right)
        {
            return -1;
        }
        int mid = (left + right) / 2;
        if (nums[mid] < target)
        {
            return this->rSearchRange(nums, target, mid + 1, right, find_first);
        }
        else if (nums[mid] > target)
        {
            return this->rSearchRange(nums, target, left, mid - 1, find_first);
        }
        else
        {
            if (find_first)
            {
                if (mid == left || nums[mid - 1] < target)
                {
                    // if mid is the start or the first value in nums equal to target
                    return mid;
                }
                return this->rSearchRange(nums, target, left, mid - 1, find_first);
            }
            else
            {
                if (mid == right || nums[mid + 1] > target)
                {
                    // if mid is the end or the last value in nums equal to target
                    return mid;
                }
                return this->rSearchRange(nums, target, mid + 1, right, find_first);
            }
        }
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        // trivial cases
        if (n == 0)
        {
            return vector<int>{-1, -1};
        }
        if (n == 1)
        {
            return target == nums[0] ? vector<int>{0, 0} : vector<int>{-1, -1};
        }

        int start_idx = this->rSearchRange(nums, target, 0, n - 1, true);
        if (start_idx == -1) // if target doesn't exist in nums at all
        {
            return vector<int>{-1, -1};
        }
        int end_idx = this->rSearchRange(nums, target, 0, n - 1, false);
        return vector<int>{start_idx, end_idx};
    }
};