using System;

namespace LC35
{
    class Program
    {
        public static string LongestPalindrome(string s) 
        {
            if (s.Length == 1)
            {
                return s;
            }

            string longestPalSubstr = s[0].ToString();
            int longestPalSubstrLength = 1;
            int sLength = s.Length;

            // M[i, j] represents if the substring of s from from indices i to j (inclusive) is a palindrome.
            bool[, ] M = new bool [sLength, sLength]; 
            
            // edge cases
            for (int i = 0; i < sLength; i++)
            {
                M[i, i] = true;
            }

            // Populate the rest of M.
            for (int i = sLength - 1; i >= 0; i--)
            {
                for (int j = i + 1; j < sLength; j++)
                {
                    if (j == i + 1)
                    {
                        M[i, j] = s[i] == s[j];
                    }
                    else
                    {
                        M[i, j] = (s[i] == s[j]) && M[i + 1, j - 1];
                    }

                    // Update longest palindromic substring and its length if necessary.
                    if (M[i, j] && (j - i + 1 > longestPalSubstrLength))
                    {
                        longestPalSubstrLength = j - i + 1;
                        longestPalSubstr = s.Substring(i, j - i + 1);
                    }
                }
            }
            
            return longestPalSubstr;
        }

        public static void testLPS(string s)
        {
            string lps = LongestPalindrome(s);
            Console.WriteLine(lps);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING");

            Console.Write("\nTest Case 1: ");
            testLPS("aaa");

            Console.Write("\nTest Case 2: ");
            testLPS("ada");

            Console.Write("\nTest Case 3: ");
            testLPS("babad");

            Console.Write("\nTest Case 4: ");
            testLPS("cbbd");

            Console.Write("\nTest Case 5: ");
            testLPS("qwertyuiop");

            Console.Write("\nTest Case 6: ");
            testLPS("racecarxtacocatxmadamimadam");

            Console.Write("\nTest Case 7: ");
            testLPS("xyyxz");

            Console.WriteLine("\nFINISHED");
        }

    }
}
