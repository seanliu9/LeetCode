using System;

namespace LC123
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
            int[] maxProfitUpTo = new int[n]; // maxProfitUpTo[i] denotes the max possible profit up to day i
            int minPrice = prices[0];
            for (int i = 1; i < n; i++)
            {
                if (prices[i] < minPrice)
                {
                    minPrice = prices[i];
                }
                maxProfitUpTo[i] = Math.Max(maxProfitUpTo[i - 1], prices[i] - minPrice);
            }

            int[] maxProfitFrom = new int[n]; // maxProfitFrom[i] denotes the max possible profit starting from day i
            int maxPrice = prices[n - 1];
            for (int i = n - 2; i >= 0; i--)
            {
                if (prices[i] > maxPrice)
                {
                    maxPrice = prices[i];
                }
                maxProfitFrom[i] = Math.Max(maxProfitFrom[i + 1], maxPrice - prices[i]);
            }

            // Now find the max possible profit from 2 transactions.
            int maxProfit = 0;
            for (int i = 0; i < n; i++)
            {
                maxProfit = Math.Max(maxProfit, maxProfitUpTo[i] + maxProfitFrom[i]);
            }

            return maxProfit;
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
            testMaxProfit([1, 2, 3, 4, 5]);

            Console.Write("Test Case 2: ");
            testMaxProfit([100, 80, 60, 40, 20]);

            Console.Write("Test Case 3: ");
            testMaxProfit([3, 6]);

            Console.Write("Test Case 4: ");
            testMaxProfit([9, 8]);

            Console.Write("Test Case 5: ");
            testMaxProfit([725]);

            Console.Write("Test Case 6: ");
            testMaxProfit([3, 3, 5, 0, 0, 3, 1, 4]);

            Console.Write("Test Case 7: ");
            testMaxProfit([14, 15, 17, 2, 9, 15, 12]);

            Console.WriteLine("\nFINISHED");
        }
    }
}
