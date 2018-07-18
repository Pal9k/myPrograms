// 3. Write a Java program that displays area of different Figures(Rectangle,Square,Triangle)
// using the method overloading.

import java.util.Scanner;

class Figures
{
	double area(double l,double w)
	{
		return l*w;
	}

	double area(double l)
	{
		return l*l;
	}

	double area(int l,int b)
	{
		return (1/2.0)*l*b;
	}
}

class FiguresDemo
{
	public static void main(String[] args) {
		Figures f = new Figures();
		// area of circle
		System.out.println("The area of circle is "+f.area(10));
		// area of triangle
		System.out.println("The area of triangle is "+f.area(10,10));
		// area of ractangle
		System.out.println("The area of ractangle is "+f.area(10.0,5));
	}
}