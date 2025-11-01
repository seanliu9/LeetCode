using System;

namespace LC115
{
    class Program
    {

        public static int NumDistinct(string s, string t) {
            int n = s.Length;
            int m = t.Length;
            if (n < m)
            {
                return 0;
            }

            int[, ] M = new int[n, m]; // M[i, j] denotes the number of distinct subsequences of s[0, i] that equal t[0, j]

            // base cases

            M[0, 0] = s[0] == t[0] ? 1 : 0;

            // Populate the leftmost column of M.
            for (int i = 1; i < n; i++)
            {     
                if (t[0] == s[i])
                {
                    M[i, 0] = M[i - 1, 0] + 1;
                }
                else
                {
                    M[i, 0] = M[i - 1, 0];
                }
            }

            // Populate the rest of M. Note that int initially defaults to 0.
            for (int i = 1; i < n; i++)
            {
                for (int j = 1; j <= Math.Min(i, m - 1); j++)
                {
                    if (s[i] != t[j])
                    {
                        M[i, j] = M[i - 1, j];
                    }
                    else
                    {
                        M[i, j] = M[i - 1, j - 1] + M[i - 1, j];
                    }
                }
            }

            return M[n - 1, m - 1];
        }

        public static void testNumDistinct(string s, string t)
        {
            int numDistinct = NumDistinct(s, t);
            Console.WriteLine(numDistinct);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING:\n");

            Console.Write("Test Case 1: ");
            testNumDistinct("rabbbit", "rabbit");

            Console.Write("Test Case 2: ");
            testNumDistinct("babgbag", "bag");

            Console.Write("Test Case 3: ");
            testNumDistinct("b", "b");

            Console.Write("Test Case 4: ");
            testNumDistinct("b", "a");

            Console.Write("Test Case 5: ");
            testNumDistinct("b", "ab");

            Console.Write("Test Case 6: ");
            testNumDistinct("exercise", "e");

            Console.Write("Test Case 7: ");
            testNumDistinct("hawaii", "ai");

            Console.Write("Test Case 8: ");
            testNumDistinct("abbcabab", "ab");

            Console.WriteLine("\nFINISHED");
        }
    }
}
