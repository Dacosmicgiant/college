package myPackage;

	interface Area
	{
		double pi=3.142;
		void compute();
	interface Volume
	{
		void compute();
	}

	public class Sphere implements Area,Volume
{
	public double r;
	public void compute()
	{
		System.out.println("area of sphere= "+(4.0*pi*r*r));
		System.out.println("volume of sphere= "+(4.0/3*pi*r*r*r));
	}
}