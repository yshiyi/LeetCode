# String
<!-- GFM-TOC -->
* [Leetcode Array](#Array)
    * [1. Introduction to String](#1-Introduction-to-String)
       * [1.1 Compare Function](#1-.-1-Compare-Function)
       * [1.2 Immutable or Mutable]
       * [1.3 Extra Operation]
       * [1.4 Time Complexity]
<!-- GFM-TOC -->


# 1. Introduction to String
## 1.1 Compare Function
Use "==" to compare two strings in both C++ and python.
```
int main() {
    string s1 = "Hello World";
    cout << "s1 is \"Hello World\"" << endl;
    string s2 = s1;
    cout << "s2 is initialized by s1" << endl;
    string s3(s1);
    cout << "s3 is initialized by s1" << endl;
    // compare by '=='
    cout << "Compared by '==':" << endl;
    cout << "s1 and \"Hello World\": " << (s1 == "Hello World") << endl; // 1
    cout << "s1 and s2: " << (s1 == s2) << endl; // 1
    cout << "s1 and s3: " << (s1 == s3) << endl; // 1
    // compare by 'compare'
    cout << "Compared by 'compare':" << endl;
    cout << "s1 and \"Hello World\": " << !s1.compare("Hello World") << endl; // 1
    cout << "s1 and s2: " << !s1.compare(s2) << endl; // 1
    cout << "s1 and s3: " << !s1.compare(s3) << endl; // 1
}
```
## 1.2 Immutable or Mutable
Immutable means that you can't change the content of the string once it's initialized.\
In C++ and python, the string is mutable.
```
#include <iostream>

int main() {
    string s1 = "Hello World";
    s1[5] = ',';
    cout << s1 << endl;  // Hello,World
}
```
## 1.3 Extra Operation
Concatenate, find and substr
```
#include <iostream>

int main() {
    string s1 = "Hello World";
    // 1. concatenate
    s1 += "!";
    cout << s1 << endl; // Hello World!
    // 2. find
    cout << "The position of first 'o' is: " << s1.find('o') << endl; // 4
    cout << "The position of last 'o' is: " << s1.rfind('o') << endl; // 7
    // 3. get substr
    cout << s1.substr(6, 5) << endl; // World
}
```
## 1.4 Time Complexity
If the length of the string is N, the time complexity of both finding operation and substring operation is O(N).\
Never forget to take the time complexity of built-in operations into consideration when you compute the time complexity for your solution.






















