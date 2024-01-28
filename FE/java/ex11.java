import java.util.Scanner;

class MonthException extends Exception
{
	String msg;
	MonthException()
	{
		msg= new String("MonthException: Enter a number between 1 and 12");
	}
}
	
class ex11
{
	public static void main(String args[])
	{
		Scanner sc= new Scanner(System.in);
		System.out.println("enter month number: ");
		int x=sc.nextInt();

	try{
		if(x>=1 && x<=12)
		System.out.println("x is a valid month number: ");
		else
		throw new MonthException();
		}

	catch(MonthException e)
	{
		System.out.println(e.msg);
	}
}
}