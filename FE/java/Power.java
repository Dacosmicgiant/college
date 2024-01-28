import java.util.*;

class Power
{
	public static void main(String[] args)
	{
	Scanner s= new Scanner(System.in);
	int a,b;
	
	System.out.println("enter base: ");
	a=s.nextInt();
	System.out.println("enter power: ");
	b=s.nextInt();
	
	Power p=new Power();
	System.out.println("the result is: "+ p.Cal(a,b));
	}
	
	int Cal(int x, int y)
	{
	if (y==0)
	return 1;
	else
	return(x*Cal(x,y-1));
	}
} 