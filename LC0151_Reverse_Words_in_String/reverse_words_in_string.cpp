#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        stack<string> stk;
        int word_end_index = 0;
        int n = s.length();
        int i = 0;
        while (i < n)
        {
            if (s[i] != ' ')
            {
                word_end_index = i;
                while (word_end_index < n && s[word_end_index] != ' ')
                {
                    word_end_index++;
                }
                stk.push(s.substr(i, word_end_index - i));
                i = word_end_index + 1;
            }
            else
            {
                i++;
            }   
        }

        // Pop from stk to form the answer.
        string answer = "";
        while (!stk.empty())
        {
            answer += stk.top();
            answer += " ";
            stk.pop();
        }

        return answer.substr(0, answer.size() - 1);
    }
};