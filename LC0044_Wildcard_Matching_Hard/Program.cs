using System;

namespace LC44
{
    class Program
    {
        public static bool IsMatch(string s, string p) {
            int sLength = s.Length;
            int pLength = p.Length;
            bool[, ] M = new bool[sLength + 1, pLength + 1]; // M[i, j] denotes if p[j, pLength) is a valid pattern for s[i, sLength).

            // edge cases

            M[sLength, pLength] = true; // if we run out in both s and p

            // if we run out in p but not s
            for (int i = 0; i < sLength; i++)
            {
                M[i, pLength] = false;
            }

            // if we run out in s but not p
            for (int j = pLength - 1; j >= 0; j--)
            {
                if (p[j] == '*') // A '*' can correspond to the empty string.
                {
                    M[sLength, j] = true;
                }
                else // A non-'*' character in p cannot correspond to the empty string.
                {
                    for (int idx = j; idx >= 0; idx--)
                    {
                        M[sLength, idx] = false;
                    }
                    break; // exit j loop
                }
            }

            // Populate the rest of M.
            for (int i = sLength - 1; i >= 0; i--)
            {
                for (int j = pLength - 1; j >= 0; j--)
                {
                    if (p[j] == '?') // A '?' in p must correspond to a single letter in s.
                    {
                        M[i, j] = M[i + 1, j + 1];
                    }
                    else if (p[j] == '*') // A '*' in p can correspond to zero, one, or multiple letters in s.
                    {
                        M[i, j] = M[i, j + 1] || M[i + 1, j];
                    }
                    else // if p[j] is a letter
                    {
                        M[i, j] = (s[i] == p[j]) && M[i + 1, j + 1];
                    }
                }
            }

            return M[0, 0];
        }

        public static void testIsMatch(string s, string p)
        {
            bool match = IsMatch(s, p);
            Console.WriteLine(match);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("STARTING\n");

            string s = "abcbbcad";
            
            Console.Write("Test Case 1: ");
            string p1 = "?b**?d*";
            testIsMatch(s, p1);

            Console.Write("Test Case 2: ");
            string p2 = "*";
            testIsMatch(s, p2);

            Console.Write("Test Case 3: ");
            string p3 = "????????";
            testIsMatch(s, p3);

            Console.Write("Test Case 4: ");
            string p4 = "*****";
            testIsMatch(s, p4);

            Console.Write("Test Case 5: ");
            string p5 = "???????";
            testIsMatch(s, p5);

            Console.Write("Test Case 6: ");
            string p6 = "?ab**?*";
            testIsMatch(s, p6);

            Console.Write("Test Case 7: ");
            string p7 = "*c*c?*?";
            testIsMatch(s, p7);

            Console.Write("Test Case 8: ");
            string p8 = "*?*cc*ad";
            testIsMatch(s, p8);

            Console.WriteLine("\nFINISHED");
        }
    }
}
