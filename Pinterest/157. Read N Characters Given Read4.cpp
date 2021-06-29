/*
157. Read N Characters Given Read4

Description:
Given a file and assume that you can only read the file using a given method read4, 
implement a method to read n characters.
 
Method read4:
1. The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf4.
2. The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:
    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:


File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file


Method read:
By using the read4 method, implement the method read that reads n characters 
from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.
The return value is the number of actual characters read.

Definition of read:
    Parameters:	char[] buf, int n
    Returns:	int
Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:
Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". 
We read a total of 3 characters from the file, so return 3. 
Note that "abc" is the file's content, not buf. 
buf is the destination buffer that you will have to write the results to.

Example 2:
Input: file = "abcde", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "abcde". 
We read a total of 5 characters from the file, so return 5.

Example 3:
Input: file = "abcdABCD1234", n = 12
Output: 12
Explanation: After calling your read method, buf should contain "abcdABCD1234". 
We read a total of 12 characters from the file, so return 12.

Example 4:
Input: file = "leetcode", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "leetc". 
We read a total of 5 characters from the file, so return 5.
 

Note:
Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function will only be called once for each test case.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.

Similar Questions
Read N Characters Given Read4 II - Call multiple times Hard
*/

/*
Method: The basic idea of this question is that 
        
        1. read4(buf4) returns the number of characters we have read. It returns 4 if there are some other characters left.
           Or return 1, 2, or 3, depends on the number of characters left.
        2. The characters that we just read are saved in buf4. We need to transfer those characters from buf4 to buf.
        
        For the function read(), if we can read all n char then we return n.
        If the number of char that we read is less than n, then we just return the number of char we just read.
        e.g., "leetcode", n = 5
        We can read n char, then we return 5. buf = "leetc".
        If n = 10, then we just return 8, and buf = "leetcode".
        
        Time complexity: O(N), copy N charcters
        Space complexity: O(1)
*/
class Solution {
public:
    int read(char *buf, int n) {
        // copiedChars, records the number of char we have read. If copiedChars == n, we just return n or copiedChars.
        int copiedChars = 0, readChars = 4;
        char buf4[4];
        
        /*
        There are only two scenarios:
        1. n > string.size(), return string.size() which is the value of copiedChars
        2. n < string.size(), return copiedChars which is the number of chars we have red.
        */
        while (readChars == 4) {
            readChars = read4(buf4);
            // We save each char to buf while checking if copiedChars == n. This is for n < string.size().
            for (int i = 0; i < readChars; ++i) {
                if (copiedChars == n)
                    return copiedChars;
                buf[copiedChars] = buf4[i];
                ++copiedChars;    
            }    
        }
        // If n > string.size(), it means we have read all chars from buf4, then we just return copiedChars.
        return copiedChars;
    }
};
