using System;
using System.ComponentModel.DataAnnotations;

namespace LC10
{
    class Program
    {
        // This method uses dynamic programming to determine if p is a regular expression for s.
        // Star (*) means that there can be zero, one, or multiple of the preceding character, and dot (.) means a single wildcard character.
        // e.g. a*.a* is a regular expression for aabaaa
        static bool isMatchDP(string s, string p)
        {
            int sLength = s.Length;
            int pLength = p.Length;
            bool[,] M = new bool[sLength + 1, pLength + 1]; // M[i, j] denotes whether p[j, m) is a valid pattern for s[i, n).

            // Populate the boundaries of M.
            M[sLength, pLength] = true;

            // cases when we have reached the end of p but not s
            for (int i = 0; i < sLength; i++)
            {
                M[i, pLength] = false;
            }

            // cases when we have reached the end of s but not p
            for (int j = pLength - 1; j >= 0; j -= 2)
            {
                if (j >= 1 && p[j] == '*')
                {
                    M[sLength, j] = true;
                    M[sLength, j - 1] = true; // A '*' describes the character in p immediately to its left.
                }
                else
                {
                    // If we encounter a letter not followed by a '*', then the substring of p starting at such letter definitely is not a valid pattern for s[i, n).
                    for (int x = j; x >= 0; x--)
                    {
                        M[sLength, x] = false;
                    }
                    break;
                }
            }

            // Now populate the rest of M.
            bool star = false; // denotes if we found a star when scanning p
            for (int j = pLength - 1; j >= 0; j--)
            {
                star = false;
                for (int i = sLength - 1; i >= 0; i--)
                {
                    if (j > 0 && p[j] == '*') // handling '*' in p
                    {
                        star = true;
                        M[i, j] = (s[i] == p[j - 1] && M[i + 1, j + 1]) // single letter match for '*' and its preceding character
                        || (s[i] == p[j - 1] && M[i + 1, j]) // multiple letter match for '*' and its preceding character
                        || M[i, j + 1]; // empty string match for '*' and its preceding character
                        M[i, j - 1] = M[i, j];
                    }
                    else
                    {
                        bool firstMatch = s[i] == p[j] || p[j] == '.';
                        M[i, j] = firstMatch && M[i + 1, j + 1];
                    }
                }
                if (star)
                {
                    j--;
                }
            }

            /*Console.WriteLine("\n\nFinal DP Matrix:\n");
            for (int i = 0; i <= sLength; i++)
            {
                for (int j = 0; j <= pLength; j++)
                {
                    Console.Write($"{M[i, j]} ");
                }
                Console.WriteLine();
            }
            Console.WriteLine();*/

            return M[0, 0];
        }


        // This method recursively determines if p is a regular expression for s.
        static bool isMatchRecursive(string s, string p)
        {
            return rIsMatch(s, 0, p, 0);
        }

        static bool rIsMatch(string s, int i, string p, int j) // i is the index in s and j is in the index in p that we are examining
        {
            // base cases

            if (i >= s.Length && j >= p.Length) // if we have reached the end of both s and p
            {
                return true;
            }

            if (j >= p.Length && i < s.Length) // if we have reached the end of p but not s
            {
                return false;
            }

            if (i >= s.Length && j < p.Length) // if we run out in s but not p
            {
                // Check if the rest of p is entirely sequences of a character followed by a '*' (e.g. 'b*b*a*').
                for (int idx = j; idx < p.Length; idx += 2)
                {
                    if (idx + 1 >= p.Length || p[idx + 1] != '*')
                    {
                        return false;
                    }
                }
                return true;
            }

            bool firstMatch = s[i] == p[j] || p[j] == '.';

            // Handle the case where the next character in p is '*'. 
            // We check both cases: the '*' and its preceding character (e.g. a*) correspond to the empty string in s, or they do not.
            if (p.Length > j + 1 && p[j + 1] == '*')
            {
                return rIsMatch(s, i, p, j + 2) || // move to the character in p immediately after the '*'
                 (firstMatch && rIsMatch(s, i + 1, p, j)); // assuming that the '*' and its preceding character actually correspond to something in s
            }

            // Proceed to check the next pair of characters as normal.
            if (firstMatch)
            {
                return rIsMatch(s, i + 1, p, j + 1);
            }

            return false;
        }

        static void testRecursive(string s, string p)
        {
            bool match = isMatchRecursive(s, p);
            Console.WriteLine(match);
        }

        static void testDP(string s, string p)
        {
            bool match = isMatchDP(s, p);
            Console.WriteLine(match);
        }

        static void Main(String[] args)
        {
            Console.WriteLine("STARTING\n");
            Console.WriteLine("Testing recursive method:\n");

            Console.Write("Test Case 1: ");
            string s1 = "aabaaa";
            testRecursive(s1, "a*.a*");

            Console.Write("\nTest Case 2: ");
            testRecursive(s1, ".a*b*a*a");

            Console.Write("\nTest Case 3: ");
            testRecursive(s1, ".a*b*a*");

            Console.Write("\nTest Case 4: ");
            testRecursive(s1, "......");

            Console.Write("\nTest Case 5: ");
            testRecursive(s1, "a*b*.b*a*b*a*a*b*b*a*");

            Console.Write("\nTest Case 6: ");
            testRecursive(s1, "aabaaaa");

            Console.Write("\nTest Case 7: ");
            testRecursive(s1, "baa*b*a*b*");

            Console.Write("\nTest Case 8: ");
            testRecursive(s1, ".a*a*b*a*a*.aa*b*b*b*a*b*");

            Console.Write("\nTest Case 9: ");
            testRecursive(s1, "..a.b*a*");

            Console.Write("\nTest Case 10: ");
            testRecursive(s1, ".....");

            Console.WriteLine("\nTesting dynamic programming method:\n");

            Console.Write("\nTest Case 11: ");
            testDP(s1, "a*.a*");

            Console.Write("\nTest Case 12: ");
            testDP(s1, ".a*b*a*a");

            Console.Write("\nTest Case 13: ");
            testDP(s1, ".a*b*a*");

            Console.Write("\nTest Case 14: ");
            testDP(s1, "......");

            Console.Write("\nTest Case 15: ");
            testDP(s1, "a*b*.b*a*b*a*a*b*b*a*");

            Console.Write("\nTest Case 16: ");
            testDP(s1, "aabaaaa");

            Console.Write("\nTest Case 17: ");
            testDP(s1, "baa*b*a*b*");

            Console.Write("\nTest Case 18: ");
            testDP(s1, ".a*a*b*a*a*.aa*b*b*b*a*b*");

            Console.Write("\nTest Case 19: ");
            testDP(s1, "..a.b*a*");

            Console.Write("\nTest Case 20: ");
            testDP(s1, ".....");

            Console.WriteLine("\nFINISHED");
        }
    }
}
