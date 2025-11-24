public class LC41
{
    public static int FirstMissingPositive(int[] nums)
    {
        int n = nums.Length;

        // trivial case
        if (n == 1)
        {
            return nums[0] == 1 ? 2 : 1;
        }

        int temp = 0;
        int correctIndex = 0;
        for (int i = 0; i < n; i++)
        {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i])
            {
                // Swap nums[i] and nums[nums[i] - 1], so that the value at nums[i] gets moved to the correct index.
                correctIndex = nums[i] - 1;
                temp = nums[i];
                nums[i] = nums[correctIndex];
                nums[correctIndex] = temp;
            }
        }

        // Now iterate through the array, and when we see the first index i where nums[i] does not equal i + 1, we know that i + 1 is the first missing positive integer.
        for (int i = 0; i < n; i++)
        {
            if (nums[i] != i + 1)
            {
                return i + 1;
            }
        }

        // At this point, we have not found a mismatch (see above array), so we return the next positive integer.
        return n + 1;
    }

    public static void test1()
    {
        Console.WriteLine("\nStarting test 1");
        int[] nums = { 4 };
        Console.WriteLine(LC41.FirstMissingPositive(nums));
        Console.WriteLine("Finished test 1\n");
    }

    public static void test2()
    {
        Console.WriteLine("\nStarting test 2");
        int[] nums = {1, 2, 3, 4, 5, 6, 7, 8};
        Console.WriteLine(LC41.FirstMissingPositive(nums));
        Console.WriteLine("Finished test 2\n");
    }

    public static void test3()
    {
        Console.WriteLine("\nStarting test 3");
        int[] nums = { -1, 4, 2, 1, 9, 10 };
        Console.WriteLine(LC41.FirstMissingPositive(nums));
        Console.WriteLine("Finished test 3\n");
    }

    public static void test4()
    {
        Console.WriteLine("\nStarting test 4");
        int[] nums = {-3, -6, 8, 4, -1, 0, 0, 12, 1, 2, 7, 24, -122, 3225, 1, 1, 1, 1, 811, -1950};
        Console.WriteLine(LC41.FirstMissingPositive(nums));
        Console.WriteLine("Finished test 4\n");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS----------");

        LC41.test1();
        LC41.test2();
        LC41.test3();
        LC41.test4();

        Console.WriteLine("----------FINISHED TESTS----------");
    }
}
