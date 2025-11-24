using System;

namespace LC122
{
    class Program
    {
        public static int MaxProfit(int[] prices) {
            if (prices.Length == 1)
            {
                return 0;
            }
            
            int maxProfit = 0;
            for (int i = 1; i < prices.Length; i++)
            {
                if (prices[i] > prices[i - 1])
                {
                    maxProfit += prices[i] - prices[i - 1];
                }
            }

            return maxProfit;
        }

        public static void testMaxProfit(int[] prices)
        {
            int result = MaxProfit(prices);
            Console.WriteLine(result);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING:\n");

            Console.Write("Test Case 1: ");
            testMaxProfit([7, 6, 4, 3, 1]);

            Console.Write("Test Case 2: ");
            testMaxProfit([7, 1, 5, 3, 6, 4]);

            Console.Write("Test Case 3: ");
            testMaxProfit([2, 2, 3]);

            Console.Write("Test Case 4: ");
            testMaxProfit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

            Console.Write("Test Case 5: ");
            testMaxProfit([1000]);

            Console.Write("Test Case 6: ");
            testMaxProfit([4, 4, 4, 4, 4, 4, 4, 4, 4]);

            Console.Write("Test Case 7: ");
            testMaxProfit([4, 4, 4, 6, 6, 6, 2, 3, 2]);

            Console.Write("Test Case 8: ");
            testMaxProfit([25, 63, 64]);

            Console.Write("Test Case 9: ");
            testMaxProfit([514, 517, 516]);

            Console.WriteLine("\nFINISHED");
        }
    }
}
