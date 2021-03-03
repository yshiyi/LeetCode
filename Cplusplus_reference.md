## C++ Reference
* [int vs unsigned int](#-int-vs-unsigned-int)

# int vs unsigned int
A variable defined as int can be either positive or negative.\
A variable defined as unsigned int can only be non-negative.\
When comparing signed with unsigned, the compiler converts the signed value to unsigned.
For example,
```
/* This works fine. 
   When an unsigned int decreases from 0 to 1, it will be automatically converted to 2^32-1.
   -1 is also converted to unsigned, i.e. (unsigned)-1
*/
for (unsigned int i = v.size()-1; i != -1; --i) 

/* This works fine.
   (unsigned)-1 is equal to 2^32 - 1
*/
for (unsigned int j = v.size()-1; j < (unsigned)-1; --j)

/* This doesn't work.
   Since (unsigned)-1 is equal to 2^32 - 1, i will never be greater than that value.
*/
for (unsigned int i = v.size()-1; i > -1; --i) 
```
