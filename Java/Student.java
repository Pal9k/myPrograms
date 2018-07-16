import java.util.Scanner;

class Student
{
    float  sub[]=new float[6];
    float perc()
    {
        float total=0;
        for(int i=0;i<6;i++)
        {
            total=total+sub[i];
        }
        total=total/6;
        return total;
    }
}

class StudentDemo
{
    public static void main(String[] args) {
        Student s1= new Student();
        Scanner s=new Scanner(System.in);
        System.out.println("Enter marks of 6 subjects");
        for(int i=0;i<6;i++)
        {
            s1.sub[i]=s.nextFloat();
        }
        
        float per=s1.perc();
        System.out.println("The percentage of subjects is "+per+"%");
        
    }
}