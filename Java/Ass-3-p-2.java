// 2. Create a class Box and display the area of box using a method area(). 
// Initialize all the variables using Constructor and demostrate Constructor Overloading.

class Box
{
	double h;
	double w;
	double d;

	Box()
	{
		h=1;
		w=1;
		d=1;
	}

	Box(double h,double w,double d)
	{
		this.h=h;
		this.w=w;
		this.d=d;
	}
	double volume()
	{
		return h*w*d;
	}
}

class BoxDemo
{
	public static void main(String[] args) {
		Box b1 = new Box();
		Box b2 = new Box(1,2,3);

		System.out.println("The volume of box b1 is "+b1.volume());
		System.out.println("The volume of box b2 is "+b2.volume());
	}
}