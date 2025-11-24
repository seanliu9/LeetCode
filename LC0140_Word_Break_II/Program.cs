public class LC140
{
    static int NUM_LETTERS = 26; // There are 26 lowercase letters in the English alphabet.

    // This method computes the hash of a string. For example, the hash of "cat" is c * 26^2 + a * 26^1 + t * 26^0
    public static int hash(string s)
    {
        int n = s.Length;
        int result = 0;
        int currFactor = 1;
        for (int i = n - 1; i >= 0; i--)
        {
            result += currFactor * (int)s[i];
            currFactor *= NUM_LETTERS;
        }
        return result;
    }

    // This solution uses backtracking.
    public static void rSolveBT(string s, HashSet<int> wordSet, int cutIndex, IList<string> currList, IList<string> answer)
    {
        // base case
        if (cutIndex == s.Length)
        {
            answer.Add(string.Join(" ", currList));
            return;
        }

        // backtracking
        string currSubstring = null;
        for (int i = cutIndex + 1; i <= s.Length; i++)
        {
            // Check if the hash of the substring of s from indices cutIndex to i (both inclusive) belongs in wordSet.
            currSubstring = s.Substring(cutIndex, i - cutIndex);
            if (wordSet.Contains(LC140.hash(currSubstring)))
            {
                currList.Add(currSubstring);

                // Recurse on the substring to the right of the cut.
                LC140.rSolveBT(s, wordSet, i, currList, answer);

                // Remove the last added string from currAnswer.
                currList.RemoveAt(currList.Count - 1);
            }
        }
    }

    public static IList<string> WordBreakBT(string s, IList<string> wordDict)
    {
        // Compute the hash of every string in wordDict, and add them to a set.
        HashSet<int> wordSet = new HashSet<int>();
        foreach (string word in wordDict)
        {
            wordSet.Add(LC140.hash(word));
        }

        IList<string> currList = new List<string>();
        IList<string> answer = new List<string>();
        LC140.rSolveBT(s, wordSet, 0, currList, answer);

        return answer;
    }

    public static IList<string> WordBreakDP(string s, IList<string> wordDict)
    {
        // Find the length of the longest word in wordDict.
        int maxLength = -1;
        int minLength = Int32.MaxValue;
        int currLength = 0;
        foreach (string word in wordDict)
        {
            currLength = word.Length;
            maxLength = Math.Max(maxLength, currLength);
            minLength = Math.Min(minLength, currLength);
        }

        /* Separate words in wordDict by length. Create a dictionary that maps a length to a set of hashes of all the words of that length.
        This is to avoid any hash collisions between different words.
        e.g. hashesDict[3] is a set of hashes of all the words of length 3 */
        Dictionary<int, HashSet<int>> hashesDict = new Dictionary<int, HashSet<int>>();
        foreach (string word in wordDict)
        {
            currLength = word.Length;
            // Create a new hashset for the current word's length if it's the first time we see a word of this length.
            if (!hashesDict.ContainsKey(currLength))
            {
                hashesDict[currLength] = new HashSet<int>();
            }
            hashesDict[currLength].Add(LC140.hash(word));
        }

        int n = s.Length;
        // T[i] = list of valid sentences equal to the substring of s from index 0 to i - 1 (inclusive). Our final answer is T[n].
        IList<string>[] T = new List<String>[n + 1];

        // base case
        T[0] = new List<string> { "" }; 
        
        // recurrence- the idea is to keep track of our last valid cut index
        List<string> currList = new List<string>();
        int startIndex = 0;
        string currSubstring = null;
        int currHash = 0;
        for (int i = 1; i <= n; i++)
        {
            currList = new List<string>();
            for (int length = minLength; length <= maxLength && i - length >= 0; length++)
            {
                startIndex = i - length;
                if (hashesDict.ContainsKey(length))
                {
                    currSubstring = s.Substring(startIndex, length);
                    currHash = LC140.hash(currSubstring);
                    if (hashesDict[length].Contains(currHash) && T[startIndex] != null) // if currSubstring is a word in wordDict
                    {
                        foreach (string str in T[startIndex])
                        {
                            if (str == "")
                            {
                                currList.Add(currSubstring);
                            }
                            else
                            {
                                currList.Add(str + " " + currSubstring);
                            }
                        }
                    }
                }
            }
            T[i] = currList;
        }

        return T[n] ?? new List<string>();
    }

    public static void printList(IList<string> stringList)
    {
        foreach (string str in stringList)
        {
            Console.WriteLine(str);
        }
    }

    public static void test1BT()
    {
        Console.WriteLine("\nStarting test 1 (backtracking)");

        string s = "catsanddog";
        IList<string> wordDict = ["cat", "cats", "and", "sand", "dog"];
        IList<string> answer = LC140.WordBreakBT(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 1 (backtracking)\n");
    }

    public static void test2BT()
    {
        Console.WriteLine("\nStarting test 2 (backtracking)");

        string s = "pineapplepenapple";
        IList<string> wordDict = ["apple", "pen", "applepen", "pine", "pineapple"];
        IList<string> answer = LC140.WordBreakBT(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 2 (backtracking)\n");
    }

    public static void test3BT()
    {
        Console.WriteLine("\nStarting test 3 (backtracking)");

        string s = "catsandog";
        IList<string> wordDict = ["cats", "dog", "sand", "and", "cat"];
        IList<string> answer = LC140.WordBreakBT(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 3 (backtracking)\n");
    }

    public static void test4BT()
    {
        Console.WriteLine("\nStarting test 4 (backtracking)");

        string s = "catsandog";
        IList<string> wordDict = ["cats", "dog", "sand", "and", "cat", "san"];
        IList<string> answer = LC140.WordBreakBT(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 4 (backtracking)\n");
    }

    public static void test5BT()
    {
        Console.WriteLine("\nStarting test 5 (backtracking)");

        string s = "catsanddog";
        IList<string> wordDict = ["cats", "dog", "sand", "and", "cat", "s"];
        IList<string> answer = LC140.WordBreakBT(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 4 (backtracking)\n");
    }

    public static void test1DP()
    {
        Console.WriteLine("\nStarting test 1 (DP)");

        string s = "catsanddog";
        IList<string> wordDict = ["cat", "cats", "and", "sand", "dog"];
        IList<string> answer = LC140.WordBreakDP(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 1 (DP)\n");
    }

    public static void test2DP()
    {
        Console.WriteLine("\nStarting test 2 (DP)");

        string s = "pineapplepenapple";
        IList<string> wordDict = ["apple", "pen", "applepen", "pine", "pineapple"];
        IList<string> answer = LC140.WordBreakDP(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 2 (DP)\n");
    }

    public static void test3DP()
    {
        Console.WriteLine("\nStarting test 3 (DP)");

        string s = "catsandog";
        IList<string> wordDict = ["cats", "dog", "sand", "and", "cat"];
        IList<string> answer = LC140.WordBreakDP(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 3 (DP)\n");
    }

        public static void test4DP()
    {
        Console.WriteLine("\nStarting test 4 (DP)");

        string s = "catsandog";
        IList<string> wordDict = ["cats", "dog", "sand", "and", "cat", "san"];
        IList<string> answer = LC140.WordBreakDP(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 4 (DP)\n");
    }

    public static void test5DP()
    {
        Console.WriteLine("\nStarting test 5 (DP)");

        string s = "catsanddog";
        IList<string> wordDict = ["cats", "dog", "sand", "and", "cat", "s"];
        IList<string> answer = LC140.WordBreakDP(s, wordDict);
        LC140.printList(answer);

        Console.WriteLine("Finished test 5 (DP)\n");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS (BACKTRACKING)----------");

        LC140.test1BT();
        LC140.test2BT();
        LC140.test3BT();
        LC140.test4BT();
        LC140.test5BT();

        LC140.test1DP();
        LC140.test2DP();
        LC140.test3DP();
        LC140.test4DP();
        LC140.test5DP();

        Console.WriteLine("----------FINISHED TESTS (BACKTRACKING)----------");
    }
}
