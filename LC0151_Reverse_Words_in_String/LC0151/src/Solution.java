import java.util.Stack;
class Solution {
    public String reverseWords(String s) {
        Stack<String> stk = new Stack<String>();
        int n = s.length();
        int word_end_index = 0;
        int i = 0;
        while (i < n)
        {
            if (s.charAt(i) != ' ')
            {
                // Scan s starting at i for an entire word.
                word_end_index = i;
                while (word_end_index < n && s.charAt(word_end_index) != ' ')
                {
                    word_end_index++;
                }
                // Now we have found an entire word.
                stk.push(s.substring(i, word_end_index));
                i = word_end_index + 1;
            }
            else
            {
                i++;
            }
        }
        // Now construct the answer by popping off the stack.
        String answer = "";
        while (!stk.isEmpty())
        {
            answer += stk.pop();
            answer += " ";
        }
        return answer.substring(0, answer.length() - 1);
    }
}