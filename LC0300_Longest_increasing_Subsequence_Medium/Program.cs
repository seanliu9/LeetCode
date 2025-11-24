using System;

namespace LC300
{
    class Program
    {
        public static int LengthOfLIS(int[] nums) 
        {
            int[] lis = new int[nums.Length]; // lis[i] is the length of the longest increasing subsequence in nums ending at index i
            for (int i = 0; i < lis.Length; i++)
            {
                lis[i] = 1;
            }

            int maxLISLength = 1;
            for (int i = 1; i < nums.Length; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    if (nums[j] < nums[i] && lis[j] + 1 > lis[i])
                    {
                        lis[i] = lis[j] + 1;
                    }
                }
                if (lis[i] > maxLISLength)
                {
                    maxLISLength = lis[i];
                }
            }
            return maxLISLength;
        }

        static void testLIS(int[] arr)
        {
            int LISLength = LengthOfLIS(arr);
            Console.WriteLine(LISLength);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING");

            Console.Write("\nTest Case 1: ");
            testLIS([4, 10, 4, 3, 8, 9]);;

            Console.Write("\nTest Case 2: ");
            testLIS([1, 3, 2, 5, 5, 9, 7]);

            Console.Write("\nTest Case 3: ");
            testLIS([7, 6, 5, 4, 3, 2, 1]);

            Console.Write("\nTest Case 4: ");
            testLIS([100, 200, 300, 400, 500]);

            Console.Write("\nTest Case 5: ");
            testLIS([10, 9, 2, 5, 3, 7, 101, 18]);

            Console.WriteLine("\nFINISHED");
        }

    }
}

