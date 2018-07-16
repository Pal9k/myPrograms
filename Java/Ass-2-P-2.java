//2. Write a program to accept a line and check how many consonants and vowels are there in line.                   
//3. Write a program to count the number of words that start with capital letters.

import java.util.Scanner;

import javax.lang.model.util.ElementScanner6;

class Demo
{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String str = s.nextLine();
        int vowels=0;
        int consonants=0;
        boolean flag=true;
        int words=0;

        for(int i=0;i<str.length();i++)
        {
            Character c=new Character(str.charAt(i));
            if(c=='a'  || c=='e' || c=='i' || c=='o' || c=='u')
            {
                vowels++;
            }
            else if(c!=' '){
                consonants+=1;
            }
            if(Character.isUpperCase(c)){
                if(flag)
                    words+=1;
                flag=false;
            }
            if(c==' ')
                flag=true;
            
        }
        System.out.println("Vowels = "+vowels+"\nConsonants = "+consonants);
        lSystem.out.println("Words = "+words);

    }
}