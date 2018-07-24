import java.util.Scanner;

class A
{
    void getdescription()
    {
        System.out.println("Class A");
    }
}

class B extends A
{
    void getdescription()
    {
        super.getdescription();
        System.out.println("Class B");
    }
}

class C extends B
{
    void getdescription()
    {
        super.getdescription();
        System.out.println("Class C");
    }
}

class ADemo
{
    public static void main(String[] args) {
        C c=new C();
        c.getdescription();
    }
}

