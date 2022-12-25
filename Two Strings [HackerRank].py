'''
--------------------------------------------------------------------------------------------------------------
Given two strings, determine if they share a common substring. A substring may be as small as one character.
Example:
s1='and'
s2='art'
These share the common substring a.
s1='be'
s2='cat'
These do not share a substring.
--------------------------------------------------------------------------------------------------------------
Function Description:
Complete the function twoStrings in the editor below.
twoStrings has the following parameter(s):
string s1: a string
string s2: another string
--------------------------------------------------------------------------------------------------------------
Returns:
string: either YES or NO
--------------------------------------------------------------------------------------------------------------
Input Format:
The first line contains a single integer p, the number of test cases.
The following p pairs of lines are as follows:
The first line contains string s1.
The second line contains string s2.
--------------------------------------------------------------------------------------------------------------
Constraints:
s1 and s2 consist of characters in the range ascii[a-z].
1 <= p <= 10
1 <= |s1|,|s2| <= 10^5
--------------------------------------------------------------------------------------------------------------
Output Format:
For each pair of strings, return YES or NO.
--------------------------------------------------------------------------------------------------------------
Sample Input:
2
hello
world
hi
world
--------------------------------------------------------------------------------------------------------------
Sample Output:
YES
NO
--------------------------------------------------------------------------------------------------------------
Explanation:
We have p=2 pairs to check:
1. s1="hello",s2="world". The substrings "o" and "l" are common to both strings.
2. a="hi", b="world". s1 and s2 share no common substrings.
--------------------------------------------------------------------------------------------------------------
'''
################################################################################################################################################################################
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    return 'YES' if set(s1) & set(s2) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
