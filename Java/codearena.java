/*
Maga and Alex are good at string manipulation problems. Just now they have faced a problem related to string. But it is not a standard string problem. They have no idea to solve it. They need your help.

A string is called unique if all characters of string are distinct.

String  is called subsequence of string  if  can be produced from by removing some characters of .

String  is stronger than  if  is lexicographically greater than .

You are given a string. Your task is to find the strongest unique string which is subsequence of given string.

Input:

first line contains length of string.
second line contains the string.

Output:

Output the strongest unique string which is subsequence of given string.
*/

import java.util.Scanner;
public class TestClass {  
      public static void main(String a[]) {  
           Scanner sc = new Scanner(System.in);  
           int count = sc.nextInt();  
 
           String str = sc.nextLine();  

           List<String> list = new ArrayList<String>();  
           for (int i = 0; i < str.length(); i = i + 1) {  
                if (str.length() - i >= count) {  
                     list.add(str.substring(i, count + i));  
                }  
           }  
           Collections.sort(list);  
           System.out.println(list.get(list.size() - 1));  
      }  
 }