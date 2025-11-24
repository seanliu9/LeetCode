using System;

namespace LC87
{
    class Program
    {

        public static bool IsScramble(string s1, string s2) {
            int n = s1.Length;
            // M[i, j, k] denotes if s1[i, i + k] can be scrambled to create s2[j, j + k]. Our goal is to compute M[0, 0, n - 1].
            bool[, ,] M = new bool[n, n, n]; 

            // base cases
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    M[i, j, 0] = s1[i] == s2[j]; // when k = 0
                }
            }

            // Populate the rest of M.
            for (int k = 1; k < n; k++) // all possible values of k
            {
                for (int i = 0; i < n - k; i++) // all possible starting indices in str1
                {
                    for (int j = 0; j < n - k; j++) // all possible starting indices in str2
                    {
                        for (int splitIndex = 0; splitIndex < k; splitIndex++) // all possible split indices in str1
                        {
                            // if we don't swap the two parts of str1
                            if (M[i, j, splitIndex] && M[i + splitIndex + 1, j + splitIndex + 1, k - splitIndex - 1]) 
                            {
                                M[i, j, k] = true;
                                break; // exit splitIndex loop
                            }
                            // if we do swap the two parts of str1
                            if (M[i, j + k - splitIndex, splitIndex] && M[i + splitIndex + 1, j, k - splitIndex - 1])
                            {
                                M[i, j, k] = true;
                                break; // exit splitIndex loop
                            }
                        }
                    }
                }
            }

            return M[0, 0, n - 1];
        }

        public static void testIsScramble(string s1, string s2)
        {
            bool result = IsScramble(s1, s2);
            Console.WriteLine(result);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING\n");

            Console.Write("Test Case 1: ");
            testIsScramble("great", "rgeat");

            Console.Write("Test Case 2: ");
            testIsScramble("a", "a");

            Console.Write("Test Case 3: ");
            testIsScramble("abcdefg", "abcdefg");

            Console.Write("Test Case 4: ");
            testIsScramble("abcde", "caebd");

            Console.Write("Test Case 5: ");
            testIsScramble("networking", "gkinorentw");

            Console.Write("Test Case 6: ");
            testIsScramble("apple", "banana");
        }
    }
}