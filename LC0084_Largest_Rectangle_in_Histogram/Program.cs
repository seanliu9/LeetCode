public class LC84
{
    public static int LargestRectangleArea(int[] heights)
    {
        int n = heights.Length;
        // trivial case- if heights consists of only 1 bar
        if (n == 1)
        {
            return heights[0];
        }

        // leftBoundaries[i] = first index to the left of i whose height is less than heights[i]
        int[] leftBoundaries = new int[n];
        Stack<int> stack = new Stack<int>();

        // Populate leftBoundaries.
        for (int i = 0; i < n; i++)
        {
            while (stack.Count > 0 && heights[stack.Peek()] >= heights[i])
            {
                stack.Pop();
            }
            leftBoundaries[i] = stack.Count == 0 ? 0 : stack.Peek() + 1;
            stack.Push(i);
        }

        // rightBoundaries[i] = first index to the right of i whose height is less than heights[i]
        int[] rightBoundaries = new int[n];
        stack.Clear();

        // Populate rightBoundaries.
        for (int i = n - 1; i >= 0; i--)
        {
            while (stack.Count > 0 && heights[stack.Peek()] >= heights[i])
            {
                stack.Pop();
            }
            rightBoundaries[i] = stack.Count == 0 ? n - 1 : stack.Peek() - 1;
            stack.Push(i);
        }

        // Now find the area of the largest rectangle in the histogram.
        int maxRectangleArea = -1;
        int currRectangleArea = 0;
        for (int i = 0; i < n; i++)
        {
            currRectangleArea = (rightBoundaries[i] - leftBoundaries[i] + 1) * heights[i];
            maxRectangleArea = Math.Max(maxRectangleArea, currRectangleArea);
        }

        return maxRectangleArea;
    }

    public static void test1()
    {
        Console.WriteLine("\nStarting test 1:");
        int[] heights = { 2, 1, 5, 6, 2, 3 };
        int maxArea = LC84.LargestRectangleArea(heights);
        Console.WriteLine(maxArea);
        Console.WriteLine("Finished test 1\n");
    }

    public static void test2()
    {
        Console.WriteLine("\nStarting test 2:");
        int[] heights = { 2, 4 };
        int maxArea = LC84.LargestRectangleArea(heights);
        Console.WriteLine(maxArea);
        Console.WriteLine("Finished test 2\n");
    }

    public static void test3()
    {
        Console.WriteLine("\nStarting test 3:");
        int[] heights = { 50, 50, 50, 50, 50 };
        int maxArea = LC84.LargestRectangleArea(heights);
        Console.WriteLine(maxArea);
        Console.WriteLine("Finished test 3\n");
    }

    public static void test4()
    {
        Console.WriteLine("\nStarting test 4:");
        int[] heights = { 1, 2, 3, 4, 5};
        int maxArea = LC84.LargestRectangleArea(heights);
        Console.WriteLine(maxArea);
        Console.WriteLine("Finished test 4\n");
    }

    public static void test5()
    {
        Console.WriteLine("\nStarting test 5:");
        int[] heights = { 5, 4, 3, 2, 1 };
        int maxArea = LC84.LargestRectangleArea(heights);
        Console.WriteLine(maxArea);
        Console.WriteLine("Finished test 5\n");
    }

    public static void test6()
    {
        Console.WriteLine("\nStarting test 6:");
        int[] heights = { 7, 4, 4, 6, 2, 1, 1000 };
        int maxArea = LC84.LargestRectangleArea(heights);
        Console.WriteLine(maxArea);
        Console.WriteLine("Finished test 6\n");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS----------");

        LC84.test1();
        LC84.test2();
        LC84.test3();
        LC84.test4();
        LC84.test5();
        LC84.test6();

        Console.WriteLine("----------FINISHED TESTS----------");
    }
}
