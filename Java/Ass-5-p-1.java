// 3. Write a Java program that displays area of different Figures(Rectangle,Square,Triangle)
// using the method overloading.

import java.util.Scanner;

abstract class Figures
{
	abstract double area();
}

class Circle extends Figures
{
    double rad;

    double area()
    {
        Scanner s=new Scanner(System.in);
        System.out.print("Enter radius:");
        rad=s.nextDouble();
        return 3.14*rad*rad;
    }
}

class Rectangle extends Figures
{
    double l,b;

    double area()
    {
        Scanner s=new Scanner(System.in);
        System.out.print("Enter lenght:");
        l=s.nextDouble();
        System.out.print("Enter bridht:");
        b=s.nextDouble();

        return l*b;
    }
}

class FiguresDemo
{
    public static void main(String[] args) {
        Figures f;
		f=new Circle();
		// area of circle
        System.out.println("The area of circle is "+f.area());
        f=new Rectangle();
		// area of ractangle
		System.out.println("The area of ractangle is "+f.area());
	}
}