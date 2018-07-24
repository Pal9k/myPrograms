//Write a java program to calculate gross salary & net salary taking the following data.
//Input:empno,empname,basic
// Process:
// DA=50%of basic, HRA=25%of basic, CCA=Rs240/-, PF=10%of basic, PT=Rs100/- 
// gross salary = basic + HRA + DA
// net salary = gross - PT -CCA -PF        
import java.util.Scanner;

class Emp
{
	int empno;
	String empname;
	double basic;
	double da;
	double hra;
	double cca=240;
	double pf;
	double pt=100;
	double gross;
	double net;

	void init()
	{
		da=(50/100.0)*basic;
		hra=(25/100.0)*basic;
		pf=(10/100.0)*basic;
	}

	void gross_sal()
	{
		gross = basic+hra+da;
	}

	void net_sal()
	{
		net = gross -pt -cca -pf;
	}
}

class EmpDemo
{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		Emp person = new Emp();
		System.out.println("Enter employee no.");
		person.empno=s.nextInt();
		System.out.println("Enter employee name:");
		person.empname=s.next();
		System.out.println("Enter salary:");
		person.basic=s.nextDouble();
		person.init();
		person.gross_sal();
		person.net_sal();
		System.out.println("The gross salary is "+person.gross+"\n the net salary is "+person.net);
	}

}
