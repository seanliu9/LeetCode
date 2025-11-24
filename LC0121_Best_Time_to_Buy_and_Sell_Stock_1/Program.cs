using System;

namespace LC121
{
    class Program
    {
        public static int MaxProfit(int[] prices) 
        {
            if (prices.Length == 1)
            {
                return 0;
            }
            
            int n = prices.Length;
            int[] T = new int[n]; // T[i] denotes the maximum profit we can make up to day i. Our goal is to compute T[n - 1].

            // base cases
            T[0] = 0;
            T[1] = prices[1] > prices[0] ? prices[1] - prices[0] : 0;

            // Populate the rest of T.
            int minPrice = prices[0];
            for (int i = 2; i < n; i++)
            {
                if (prices[i - 1] < minPrice)
                {
                    minPrice = prices[i - 1];
                }
                T[i] = Math.Max(T[i - 1], prices[i] - minPrice);
            }

            return T[n - 1];
        }

        public static void testMaxProfit(int[] prices)
        {
            int maxProfit = MaxProfit(prices);
            Console.WriteLine(maxProfit);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING:\n");

            Console.Write("Test Case 1: ");
            testMaxProfit([7, 1, 5, 3, 6, 4]);

            Console.Write("Test Case 2: ");
            testMaxProfit([7, 6, 4, 3, 1]);

            Console.Write("Test Case 3: ");
            testMaxProfit([500]);

            Console.Write("Test Case 4: ");
            testMaxProfit([20, 21]);

            Console.Write("Test Case 5: ");
            testMaxProfit([9, 6]);

            Console.Write("Test Case 6: ");
            testMaxProfit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

            Console.Write("Test Case 7: ");
            testMaxProfit([23, 89, 15, 17, 43, 38, 76, 62]);

            Console.WriteLine("\nFINISHED");
        }
    }
}
