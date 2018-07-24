// Write a java program that implements educational hierarchy using inheritance.
import java.util.Scanner;

class Office
{
	int empno;
	String empname;
	float salary;

	void getvalue()
	{
		Scanner s = new Scanner(System.in);
		System.out.print("Enter empno:");
		empno=s.nextInt();
		System.out.println("empno:"+empno);
		System.out.print("enter empname:");
		empname=s.next();
		System.out.println("empname:"+empname);
		System.out.print("enter salary:");
		salary=s.nextFloat();
		System.out.println("salary:"+salary);
	}
}

class Teaching extends Office
{
	String designition;
	void setvalue()
	{
		Scanner s=new Scanner(System.in);
		System.out.print("enter Designition for teaching:");
		designition=s.next();
		System.out.println("Designition(Teaching):"+designition);
	}
}

class Non_Teaching extends Office
{
	String designition;
	void setvalue()
	{
		Scanner s=new Scanner(System.in);
		System.out.print("enter Designition for non_teaching:");
		designition=s.next();
		System.out.println("Designition(Non_teaching):"+designition);
	}
}

class OfficeDemo
{
	public static void main(String[] args) {
		Teaching obj1=new Teaching();
		System.out.println("Teaching:");
		obj1.getvalue();
		obj1.setvalue();
		
		Non_Teaching obj2=new Non_Teaching();
		System.out.println("Non_Teaching:");
		obj2.getvalue();
		obj2.setvalue();
	}
}