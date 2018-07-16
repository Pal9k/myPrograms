//4. Write a program to find that given number or string is palindrome or not.

import java.util.Scanner;

class palin
{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String str = s.next();
        int len=str.length();
        boolean flag=true;

        for(int i=0;i<len/2;i++)
        {
            if(str.charAt(i)!=str.charAt(len-i-1))
            {
                flag=false;
                break;
            }
        }
        if(flag)
            System.out.println(str+" is palindrom");
        else
            System.out.println(str+" is not palindrom");
    }
}