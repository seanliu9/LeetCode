class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int max_length = 1;
        int curr_max_length = 1;
        for (int i = 0; i < nums.length - 1; i++)
        {
            if (nums[i] < nums[i + 1])
            {
                curr_max_length++;
            }
            else
            {
                curr_max_length = 1;
            }
            max_length = Math.max(max_length, curr_max_length);
        }
        return max_length;
    }
}
