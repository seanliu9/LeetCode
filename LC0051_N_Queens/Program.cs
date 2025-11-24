public class LC51
{
    public static void rSolve(int n, int col, IList<string> config, bool[] rows, bool[] diagonal1, bool[] diagonal2, IList<IList<string>> answer)
    {
        // base case
        if (col == n)
        {
            answer.Add(new List<string>(config));
            return;
        }
        // backtracking
        char[] temp = new char[n];
        for (int row = 0; row < n; row++)
        {
            /* diagonal1 refers to the / direction- note that row + col is the same for each cell in this direction. e.g. (3, 0), (2, 1), (1, 2), (0, 3). 
            This row + col value can range from 0 up to 2n.
            digonal2 refers to the \ direction- note that row - col is the same for each cell in this direction. e.g. (0, 0), (1, 1), (2, 2), (3, 3), etc. 
            This row - col value can range from -n up to n.
            Therefore, we use an array to keep track of if a diagonal is occupied (i.e. under attack) by a queen.*/
            if (!rows[row] && !diagonal1[row + col] && !diagonal2[row - col + n])
            {
                // Place a queen on the i-th row if it would not attack any existing queen (via row, column, or either diagonal)
                rows[row] = true;
                diagonal1[row + col] = true;
                diagonal2[row - col + n] = true;

                // Add this queen's placement to config.
                temp = new char[n];
                for (int i = 0; i < n; i++)
                {
                    temp[i] = '.';
                }
                temp[row] = 'Q';
                config.Add(new string(temp));

                // Recurse on the next column.
                LC51.rSolve(n, col + 1, config, rows, diagonal1, diagonal2, answer);

                // Remove the most recently placed queen.
                config.RemoveAt(config.Count - 1);
                rows[row] = false;
                diagonal1[row + col] = false;
                diagonal2[row - col + n] = false;
            }
        }

    }

    public static IList<IList<string>> SolveNQueens(int n)
    {
        // trivial cases

        if (n == 1)
        {
            return new List<IList<string>> { new List<string> { "Q" } };
        }

        // It's not possible to place 2 queens on a 2x2 chessboard or 3 queens on a 3x3 chessboard such that no two queens attack each other.
        if (n == 2 || n == 3)
        {
            return new List<IList<string>>();
        }

        IList<IList<string>> answer = new List<IList<string>>();
        IList<string> config = new List<string>();

        // Note that by default, a boolean variable initializes to false.
        bool[] rows = new bool[n];
        bool[] diagonal1 = new bool[2 * n + 1];
        bool[] diagonal2 = new bool[2 * n + 1];

        LC51.rSolve(n, 0, config, rows, diagonal1, diagonal2, answer);
        return answer;
    }

    public static void testSolution()
    {
        Console.WriteLine("\nStarting tests");

        IList<IList<string>> answer = new List<IList<string>>();
        for (int i = 1; i < 10; i++)
        {
            answer = LC51.SolveNQueens(i);
            Console.WriteLine("Answer for n = {0}:", i);
            foreach (List<string> x in answer)
            {
                Console.WriteLine(string.Join(" ", x));
            }
            Console.WriteLine("\n");
        }

        Console.WriteLine("Finished tests\n");
    }

    public static void Main(string[] args)
    {
        LC51.testSolution();
    }
}
