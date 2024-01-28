import java.util.*;

public class Array
{
	public static void main(String args[])
	{
	int n,i;
	double sum=0, avg;
	
	Scanner sc=new Scanner(System.in);
	System.out.println("enter array size: ");
	n=sc.nextInt();

	int a[]=new int[n];

	System.out.println("enter array elements: ");
	for(i=0;i<n;i++)
		{
		a[i]=sc.nextInt();
		}
	for(i=0;i<n;i++)
		{
		sum+=a[i];
		}
	avg=sum/n;
	System.out.println("Average= "+avg);
	System.out.println("Elements greater than average are: ");
	for(i=0;i<n;i++)
	{
	if(a[i]>avg)
	System.out.println(a[i]);
	}
	}
}