/*
158H. Read N Characters Given Read4 II - Call multiple times

Description:
Given a file and assume that you can only read the file using a given method read4, 
implement a method read to read n characters. Your method read may be called multiple times.
 

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
By using the read4 method, implement the method read that reads n characters from the file 
and store it in the buffer array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.
Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". 
                     We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.

Example 2:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". 
                     We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 

Note:
Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.

Similar Questions
Read N Characters Given Read4 - Easy
*/

/*
Method: The key challenge is since read4() reads 4 letters every time, how we can pass the rest of letters to next call.
        For example, "abcdefg"
        read(3), return 3. The letter 'd' has been read by read4(). The pointer is pointing at 'e'.
        We have to move the pointer back to 'd' when we call read() next round.
        
        To deal with this issue, we can create a queue.
        At the beginning of each call, if the queue is not empty, then we move the element from queue to buf.
*/

class Solution{
private:
    char buf4[4];
    queue<char> q;
public:
    int read(char *buf, int n){
        // ind is the number of character we read
        int ind = 0;
        
        // Check if there are any left over letters saved in the queue
        while(!q.empty() && n > 0){
            buf[ind] = q.front(); q.pop();
            ++ind; --n;
        }
        
        while(n>0){
            int len = read4(buf4);
            
            // Check the len
            if(len==0){
                // If there is no more letter left, we break out of the loop.
                break;
            }else if(n > len){
                // If the number of letters we need is more than 4, we push the letters to buf and deduct len from n
                for(int i=0; i<len; ++i){
                    buf[ind] = buf4[i];
                    ++ind;
                }
                n -= len;
            }else{
                // If n < len, we don't need all 4 letters. There are some letters left that we need to push them to queue.
                for(int i=0; i<n; ++i){
                    buf[ind] = buf4[i];
                    ++ind;
                }
                
                // Push the rest of letters to queue
                for(int i = n; i<len; ++i){
                    q.push(buf4[i]);
                }
                
                // Set n = 0 to break the loop.
                n = 0;
            }
            
        }
        
        return ind;
    }
}





