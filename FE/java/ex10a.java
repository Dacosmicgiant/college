import java.util.*;

interface Area
{
	double pi=3.142;
	void compute();
}
	
interface Volume
{
	double c1=4.0;
	double c2=4.0/3;
	void compute();
}

class Circle implements Area,Volume
	{
	double r;
	public void compute()
	{
		System.out.println("area of circle: " +(pi*r*r));
		
	}
}

class Sphere implements Area,Volume
{
	double r;
	public void compute()
	{
		System.out.println("Area of sphere=" +(c1*pi*r*r));
		System.out.println("Volume of sphere="+(c2*pi*r*r*r));
	}
}

class ex10a
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		Circle c=new Circle();
		Sphere s=new Sphere();

		System.out.println("Enter the radius of circle:");
		c.r=sc.nextDouble();
		c.compute();

		System.out.println("enter the radius of sphere");
		s.r=sc.nextDouble();
		s.compute();
	}

                                                                                                 }

