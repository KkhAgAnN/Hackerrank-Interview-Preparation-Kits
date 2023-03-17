import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    string = "abcdefghijklmnopqrstuvwxyz"
    if k > 26:
        k = k % 26
    num = string[:k]
    new_alphabet = string.replace(num,"")
    new_alphabet = new_alphabet + num

    new_letter = ""
    for char in s:
        if (char in string) or (char.lower() in string):
            count = 0
            is_upper = 0
            for ss in string:
                if char == ss:
                    break
                elif char == ss.upper():
                    is_upper = 1
                    break
                else:
                    count += 1
            if is_upper != 1:        
                new_letter += new_alphabet[count]
            else:
                new_letter += new_alphabet[count].upper()  
        else:
            new_letter += char
    
    return new_letter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
