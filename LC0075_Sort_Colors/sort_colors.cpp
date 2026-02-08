#include <vector>
using namespace std;

class Solution {
public:
    // Move all the elements with value target_val together.
    void sort_by_value(const int target_val, vector<int>& nums, size_t& start_idx) const {
        size_t n = nums.size();

        // Start searching for target_val from the current start_idx
        size_t target_val_idx = start_idx;

        while (target_val_idx < n && start_idx < n) {
            if (nums[start_idx] == target_val) 
            {
                start_idx++;
                if (target_val_idx < start_idx)
                {
                    target_val_idx = start_idx;
                } 
            } 
            else {
                // Find the next index in nums that has target_val, and swap it with nums[start_idx].
                if (target_val_idx <= start_idx) 
                {
                    target_val_idx = start_idx + 1;
                }
                while (target_val_idx < n && nums[target_val_idx] != target_val) 
                {
                    target_val_idx++;
                }

                if (target_val_idx < n) {
                    std::swap(nums[start_idx], nums[target_val_idx]);
                    start_idx++;
                    target_val_idx++;
                }
                else 
                {
                    break; 
                }
            }
        }
    }

    void sortColors(vector<int>& nums) {
        size_t i = 0; // i is the current index in nums we are examining
        this->sort_by_value(0, nums, i);
        this->sort_by_value(1, nums, i);
    }
};