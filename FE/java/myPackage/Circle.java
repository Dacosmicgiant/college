package myPackage;

interface Area
{
	double pi=3.142;
	void compute();
}

public class Circle implements Area
	{
		public double r;
		public void compute();
		{
			System.out.println("Area of circle: "+(pi*r*r);
		}
	}
