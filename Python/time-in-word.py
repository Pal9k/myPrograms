#!/bin/python3

import math
import os
import random
import re
import sys

dic={1:"one" , 2:"two" , 3:"three" , 4:"four" , 5:"five" , 6:"six" , 7:"seven" , 
     8:"eight" , 9:"nine" , 10:"ten" , 11:"eleven" , 12:"twelve" , 13:"thirteen" ,
     14:"fourteen" , 15:"fifteen" , 16:"sixteen" , 17:"seventeen" , 18:"eightteen" ,
     19:"ninteen" , 20:"twenty" , 21:"twenty one" , 22:"twenty two" , 23:"twenty three" ,
     24:"twenty four" , 25:"twenty five" , 26:"twenty six" , 27:"twenty seven" , 
     28:"twenty eight" , 29:"twenty nine" , 30:"thirty"}

# Complete the timeInWords function below.
def timeInWords(h, m):
    if m==0:
        return ("{} o' clock".format(dic[h]))
    elif m==15:
        return ("quarter past {}".format(dic[h]))
    elif m==30:
        return ("half past {}".format(dic[h]))
    elif m==45:
        return ("quarter to {}".format(dic[h+1]))
    elif m==1:
        return ("{} minute past {}".format(dic[m],dic[h]))
    elif m<30:
        return ("{} minutes past {}".format(dic[m],dic[h]))
    else:
        return ("{} minutes to {}".format(dic[60-m],dic[h+1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
