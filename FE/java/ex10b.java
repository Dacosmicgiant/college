import java.util.Scanner;
import myPackage.*;

class ex10b
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		Circle c= new Circle();
		Sphere s= new Sphere();

		System.out.println("enter radius of circle: ");
		c.r=sc.nextDouble();
		c.compute();
		
		System.out.println("enter the radius of sphere: ");
		s.r=sc.nextDouble();
		s.compute();
	}
}