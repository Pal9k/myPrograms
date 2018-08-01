import java.util.Scanner;

interface Interest
{
    void inti(double p,double r,double n);
}

class Simple implements Interest
{
    public void inti(double p,double r,double n)
    {
        double result=n*r*p/100;
		System.out.println("Simple Interest is "+result);   
    }
}

class Compound implements Interest
{
    public void inti(double p,double r,double n)
    {
        double result=p*(1+(r/n));
		System.out.println("Compound Interest is "+result);
    }
}

class DemoInterest{
	public static void main(String[] args) {
		Simple s = new Simple();
		Compound c = new Compound();

		s.inti(35,65,76);
		c.inti(23,34,56);
	}
}