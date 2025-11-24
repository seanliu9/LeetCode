public class LC32
{
    public static int LongestValidParentheses(string s)
    {
        int n = s.Length;
        // trivial cases- s is empty or consists of just 1 letter
        if (n < 2)
        {
            return 0;
        }

        int maxLength = 0;
        Stack<int> stack = new Stack<int>();
        stack.Push(-1);

        for (int i = 0; i < n; i++)
        {
            if (s[i] == '(')
            {
                stack.Push(i);
            }
            else // if s[i] is a ')'
            {
                stack.Pop();
                if (stack.Count == 0)
                {
                    stack.Push(i);
                }
                else
                {
                    maxLength = Math.Max(maxLength, i - stack.Peek());
                }
            }
        }

        return maxLength;
    }

    public static void test1()
    {
        Console.WriteLine("\nStarting test 1");
        string s = "";
        int maxLength = LC32.LongestValidParentheses(s);
        Console.WriteLine(maxLength);
        Console.WriteLine("Finished test 1\n");
    }

    public static void test2()
    {
        Console.WriteLine("\nStarting test 2");
        string s = "()()()()";
        int maxLength = LC32.LongestValidParentheses(s);
        Console.WriteLine(maxLength);
        Console.WriteLine("Finished test 2\n");
    }

    public static void test3()
    {
        Console.WriteLine("\nStarting test 3");
        string s = ")((())))";
        int maxLength = LC32.LongestValidParentheses(s);
        Console.WriteLine(maxLength);
        Console.WriteLine("Finished test 3\n");
    }

    public static void test4()
    {
        Console.WriteLine("\nStarting test 4");
        string s = "(())()()()())";
        int maxLength = LC32.LongestValidParentheses(s);
        Console.WriteLine(maxLength);
        Console.WriteLine("Finished test 4\n");
    }

    public static void test5()
    {
        Console.WriteLine("\nStarting test 5");
        string s = "(()";
        int maxLength = LC32.LongestValidParentheses(s);
        Console.WriteLine(maxLength);
        Console.WriteLine("Finished test 5\n");
    }

    public static void test6()
    {
        Console.WriteLine("\nStarting test 6");
        string s = "(())()";
        int maxLength = LC32.LongestValidParentheses(s);
        Console.WriteLine(maxLength);
        Console.WriteLine("Finished test 6\n");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS----------");
        
        LC32.test1();
        LC32.test2();
        LC32.test3();
        LC32.test4();
        LC32.test5();
        LC32.test6();

        Console.WriteLine("----------FINISHED TESTS----------");
    }
}
