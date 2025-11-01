package LC3LongestNonrepeatingSubstring;

import java.util.HashMap;

public class LongestNonrepeatingSubstring {

    // Find the first index of the longest nonrepeating substring in str.
    public static int findLongestNonrepeatingSubstring(String str)
    {
        int maxLength = 0;
        int startIndex = 0;
        HashMap<Character, Integer> mostRecentIndices = new HashMap<Character, Integer>(); // hashmap that maps a character to an integer

        char currChar = 0;
        for (int i = 0; i < str.length(); i++)
        {
            currChar = str.charAt(i);
            if (mostRecentIndices.containsKey(currChar))
            {
                startIndex = mostRecentIndices.get(currChar) + 1;
            }
            mostRecentIndices.put(currChar, i);
            maxLength = Math.max(maxLength, i - startIndex + 1);
        }

        return maxLength;
    }

    public static void main(String args[])
    {
        String str1 = "abcdabfcda";
        System.out.println("length of longest nonrepeating substring in str1: " + LongestNonrepeatingSubstring.findLongestNonrepeatingSubstring(str1));
        String str2 = "ababcbfghpqhb";
        System.out.println("length of longest nonrepeating substring in str2: " + LongestNonrepeatingSubstring.findLongestNonrepeatingSubstring(str2));
        String str3 = "abcdefg";
        System.out.println("length of longest nonrepeating substring in str3: " + LongestNonrepeatingSubstring.findLongestNonrepeatingSubstring(str3));
        String str4 = "xxxxx";
        System.out.println("length of longest nonrepeating substring in str4: " + LongestNonrepeatingSubstring.findLongestNonrepeatingSubstring(str4));
        String str5 = "";
        System.out.println("length of longest nonrepeating substring in str5: " + LongestNonrepeatingSubstring.findLongestNonrepeatingSubstring(str5));
    }
}
