"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
"""


def minion_game(string):
    # your code goes here
    len_str=len(string)
    stuart=0
    kevin=0
    for i in range(0,len_str):
        if (string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or         string[i]=='U'):
            kevin+=len_str-i
        else:
            stuart+=len_str-i
    if kevin>stuart:
        print("Kevin {}".format(kevin))
    else:
        print("Stuart {}".format(stuart))

if __name__ == '__main__':
    s=input()
    minion_game(s)