#include <vector>
using namespace std;

class Solution {
public:
    int rFindPeakElement(const vector<int>& nums, const size_t left, const size_t right) const
    {
        size_t mid = (left + right) / 2;
        if (((mid > left && nums[mid - 1] < nums[mid]) || mid == left) && ((mid < right && nums[mid + 1] < nums[mid]) || mid == right))
        {
            // base case: mid is a peak
            return mid;
        }
        if (nums[mid] < nums[mid + 1])
        {
            // We are on an upward slope, so the peak is to the right.
            return this->rFindPeakElement(nums, mid + 1, right);
        }
        else if (nums[mid] > nums[mid + 1])
        {
            // We are on a downward slope, so the peak is to the left.
            return this->rFindPeakElement(nums, left, mid - 1);
        }
        return -1;
    }

    int findPeakElement(vector<int>& nums) {
        size_t n = nums.size();
        if (n == 1)
        {
            return 0;
        }
        return this->rFindPeakElement(nums, 0, n - 1);
    }
};