public class LC131
{
    // This method checks if the substring of s from leftIndex to rightIndex (both inclusive) is a palindrome.
    public static bool isPalindrome(string s, int leftIndex, int rightIndex)
    {
        int left = leftIndex;
        int right = rightIndex;
        while (left < right)
        {
            if (s[left] != s[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    public static void rSolve(string s, int cutIndex, IList<string> currList, IList<IList<string>> answer)
    {
        // base case
        if (cutIndex == s.Length)
        {
            answer.Add(new List<string>(currList));
            return;
        }
        // backtracking
        for (int i = cutIndex; i < s.Length; i++)
        {
            // Check if the substring of s from indices cutIndex to i (both inclusive) is a palindrome.
            if (LC131.isPalindrome(s, cutIndex, i))
            {
                currList.Add(s.Substring(cutIndex, i - cutIndex + 1)); // Note that this is the substring starting at cutIndex, and i characters long.
                // Recurse on the substring to the right of the cut.
                LC131.rSolve(s, i + 1, currList, answer);

                // Remove the last added string to currList.
                currList.RemoveAt(currList.Count - 1);
            }
        }
    }

    public static IList<IList<string>> Partition(string s)
    {
        int n = s.Length;
        // trivial case
        if (n == 1)
        {
            return new List<IList<string>> { new List<string> { s } };
        }
        IList<string> currList = new List<string>();
        IList<IList<string>> answer = new List<IList<string>>();
        LC131.rSolve(s, 0, currList, answer);
        return answer;
    }

    public static int palindromesPartitionsCount(string s)
    {
        int n = s.Length;

        // trivial cases
        if (n == 1)
        {
            return 1;
        }
        if (n == 2)
        {
            return s[0] == s[1] ? 2 : 1;
        }

        // Find the start and end indices of all the palindromes in s, and encode them as start + n * end.
        HashSet<int> palindromeIndices = new HashSet<int>();

        int left = 0;
        int right = 0;

        // Consider palindromes where the center is a character- i.e. odd length palindromes.
        for (int center = 0; center < n; center++)
        {
            // Expand around i as the center. If the current substring is a palindrome, then we add its encoded boudary indices to palindromeIndices.
            left = center;
            right = center;
            while (left >= 0 && right < n && s[left] == s[right])
            {
                palindromeIndices.Add(left + n * right);
                left--;
                right++;
            }
        }

        // Similarly, consider palindromes where the center is a space between characters- i.e. even length palindromes.
        for (int center = 0; center < n - 1; center++)
        {
            // Expand around i as the center. If the current substring is a palindrome, then we add its encoded boudary indices to palindromeIndices.
            left = center;
            right = center + 1;
            while (left >= 0 && right < n && s[left] == s[right])
            {
                palindromeIndices.Add(left + n * right);
                left--;
                right++;
            }
        }

        // T[i, j] = # of palindromes in the substring of s starting at i and ending at j. The answer is T[0, n - 1].
        int[,] T = new int[n, n];

        // base cases
        for (int i = 0; i < n; i++)
        {
            T[i, i] = 1;
        }

        for (int i = 0; i < n - 1; i++)
        {
            T[i, i + 1] = s[i] == s[i + 1] ? 2 : 1;
        }

        int count = 0;
        for (int i = n - 2; i >= 0; i--)
        {
            for (int j = i + 2; j < n; j++)
            {
                for (int k = i; k <= j; k++)
                {
                    if (palindromeIndices.Contains(i + n * k))
                    {
                        if (k + 1 > j)
                        {
                            count++;
                        }
                        else
                        {
                            count += T[k + 1, j];
                        }
                    }
                }
                T[i, j] = count;
                count = 0;
            }
        }

        return T[0, n - 1];
    }

    public static void printLists(IList<IList<string>> lists)
    {
        foreach (IList<string> innerList in lists)
        {
            Console.WriteLine(string.Join(", ", innerList));
        }
    }

    public static void test1()
    {
        Console.WriteLine("\nStarting test 1");
        string s = "a";
        IList<IList<string>> answer = LC131.Partition(s);
        LC131.printLists(answer);
        int numPartitions = LC131.palindromesPartitionsCount(s);
        Console.WriteLine("number of palindrome partitions: {0}", numPartitions);
        Console.WriteLine("Finished test 1\n");
    }
    
    public static void test2()
    {
        Console.WriteLine("\nStarting test 2");
        string s = "banana";
        IList<IList<string>> answer = LC131.Partition(s);
        LC131.printLists(answer);
        int numPartitions = LC131.palindromesPartitionsCount(s);
        Console.WriteLine("number of palindrome partitions: {0}", numPartitions);
        Console.WriteLine("Finished test 2\n");
    }

    public static void test3()
    {
        Console.WriteLine("\nStarting test 3");
        string s = "water";
        IList<IList<string>> answer = LC131.Partition(s);
        LC131.printLists(answer);
        int numPartitions = LC131.palindromesPartitionsCount(s);
        Console.WriteLine("number of palindrome partitions: {0}", numPartitions);
        Console.WriteLine("Finished test 3\n");
    }

    public static void test4()
    {
        Console.WriteLine("\nStarting test 4");
        string s = "halloween";
        IList<IList<string>> answer = LC131.Partition(s);
        LC131.printLists(answer);
        int numPartitions = LC131.palindromesPartitionsCount(s);
        Console.WriteLine("number of palindrome partitions: {0}", numPartitions);
        Console.WriteLine("Finished test 4\n");
    }

    public static void test5()
    {
        Console.WriteLine("\nStarting test 5");
        string s = "tattoo";
        IList<IList<string>> answer = LC131.Partition(s);
        LC131.printLists(answer);
        int numPartitions = LC131.palindromesPartitionsCount(s);
        Console.WriteLine("number of palindrome partitions: {0}", numPartitions);
        Console.WriteLine("Finished test 5\n");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS----------");

        LC131.test1();
        LC131.test2();
        LC131.test3();
        LC131.test4();
        LC131.test5();

        Console.WriteLine("----------FINISHED TESTS----------");
    }
}