using System.Formats.Asn1;

public class LC30
{

    const int NUM_LETTERS = 26; // There are 26 (lowercase) letters in the English alphabet.
    public static IList<int> FindSubstring(string s, string[] words)
    {
        if (s.Length < words.Length * words[0].Length) // if s is shorter than any permutation of words
        {
            return new List<int>();
        }

        IList<int> answer = new List<int>();
        int n = s.Length;
        int w = words.Length; // w = number of strings in words
        int m = words[0].Length; // m = length of each string in words

        // Step 1: Create an array, powers, where powers[i] = 26^i.
        int[] powers = new int[m];
        int currPower = 1;
        for (int i = 0; i < m; i++)
        {
            powers[i] = currPower;
            currPower *= NUM_LETTERS;
        }

        // Step 2: Create a dictionary, mapping a string's hash to an index and its frequency in words
        // e.g. Suppose "cat" appears at indices 0 and 3 in words. The hash of "cat" is c * (26 ^ 2) + a * (26 ^ 1) + t * (26 ^ 0) = x. Thus, dict[x] = (0, 2).
        Dictionary<int, (int, int)> dict = new Dictionary<int, (int, int)>();
        int strHash = 0;
        string currWord = null;
        int numUniqueWords = 0;
        for (int i = 0; i < w; i++)
        {
            currWord = words[i];
            for (int j = 0; j < m; j++)
            {
                strHash += ((int)currWord[j]) * powers[m - 1 - j];
            }
            if (!dict.ContainsKey(strHash))
            {
                dict.Add(strHash, (numUniqueWords, 1));
                numUniqueWords++;
            }
            else
            {
                dict[strHash] = (dict[strHash].Item1, dict[strHash].Item2 + 1);
            }
            strHash = 0;
        }

        // Step 3: Create an array, rollingHashes, that stores the rolling hash for each group of m consecutive characters in s.
        // i.e. rollingHashes[i] = rolling hash of the m consecutive characters in s starting at index i
        int[] rollingHashes = new int[n - m + 1];
        // Calculate the hash of the first m characters, and after that we can apply the concept of rolling hash.
        int currHash = 0;
        for (int i = 0; i < m; i++)
        {
            currHash += ((int)s[i]) * powers[m - 1 - i];
        }
        rollingHashes[0] = currHash;
        for (int i = 1; i <= n - m; i++)
        {
            currHash = (currHash - ((int)s[i - 1]) * powers[m - 1]) * NUM_LETTERS + (int)s[i + m - 1]; // updated rolling hash
            rollingHashes[i] = currHash;
        }

        // Step 4: Use a sliding window to compare the hash of each group of m * w consecutive characters in s to the hashes obtained in Step 2.
        int[] match = new int[numUniqueWords];
        foreach (KeyValuePair<int, (int, int)> entry in dict)
        {
            match[entry.Value.Item1] = entry.Value.Item2;
        }

        int currIndex = 0;
        int currRollingHash = 0;
        int currWordIndex = 0;
        bool matchFound = true;
        for (int i = 0; i <= n - m * w; i++) // all possible starting positions of m * w characters in s
        {
            for (int j = 0; j < w; j++)
            {
                currIndex = i + j * m;
                currRollingHash = rollingHashes[currIndex];

                if (!dict.ContainsKey(currRollingHash))
                {
                    matchFound = false;
                    break; // Immediately go to the next iteration of the j loop.
                }

                currWordIndex = dict[currRollingHash].Item1;
                match[currWordIndex]--;

                if (match[currWordIndex] < 0) // checks if a string appears more times than it should
                {
                    matchFound = false;
                    break; // Immediately go to the next iteration of the j loop.
                }
            }

            if (matchFound)
            {
                answer.Add(i);
            }

            // Reset matchFound and match for the next iteration of the i loop.
            matchFound = true;
            foreach (KeyValuePair<int, (int, int)> entry in dict)
            {
                match[entry.Value.Item1] = entry.Value.Item2;
            }
        }

        return answer;
    }

    public static void test1()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 1");

        String s = "barfoothefoobarman";
        String[] words = words = ["foo", "bar"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 1");
        Console.WriteLine("***************\n");
    }

    public static void test2()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 2");

        String s = "wordgoodgoodgoodbestword";
        String[] words = ["word", "good", "best", "word"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 2");
        Console.WriteLine("***************\n");
    }

    public static void test3()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 3");

        String s = "barfoofoobarthefoobarman";
        String[] words = ["bar", "foo", "the"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 3\n");
        Console.WriteLine("***************\n");
    }

    public static void test4()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 4");

        String s = "aaaaaaaaaa"; // Note: s consists of 10 a's
        String[] words = ["a", "a"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 4");
        Console.WriteLine("***************\n");
    }

    public static void test5()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 5");

        String s = "helloworld";
        String[] words = ["world", "hello"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 5");
        Console.WriteLine("***************\n");
    }

    public static void test6()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 6");

        String s = "applepie";
        String[] words = ["apple", "pies"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 6");
        Console.WriteLine("***************\n");
    }

    public static void test7()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 7");

        String s = "abcdefgh";
        String[] words = ["f", "c", "g", "e", "d"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 7");
        Console.WriteLine("***************\n");
    }

    public static void test8()
    {
        Console.WriteLine("***************");
        Console.WriteLine("Starting test 8");

        String s = "papaya";
        String[] words = ["a"];
        IList<int> answer = LC30.FindSubstring(s, words);
        Console.WriteLine(string.Join(", ", answer));

        Console.WriteLine("Finished test 8");
        Console.WriteLine("***************\n");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS----------\n");

        LC30.test1();
        LC30.test2();
        LC30.test3();
        LC30.test4();
        LC30.test5();
        LC30.test6();
        LC30.test7();
        LC30.test8();

        Console.WriteLine("\n----------FINISHED TESTS----------");
    }
}
