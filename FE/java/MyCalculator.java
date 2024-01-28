import java.util.*;
public class MyCalculator
{
	public static void main(String[] args)
	{
	int choice,a=0,b=0;
	do
	{
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter your choice: \n 1:Add \n 2:Sub \n 3:Mul \n 4:Div \n 5:Exit");
	choice=sc.nextInt();
	switch(choice)
	{
		case 1: System.out.println("enter 2 numbers");
		a=sc.nextInt();
		b=sc.nextInt();
		System.out.println("the addition of the two numbers: "+(a+b));
		break;
		case 2: System.out.println("enter 2 numbers");
		a=sc.nextInt();
		b=sc.nextInt();
		System.out.println("the subtraction of the two numbers: "+(a-b));
		break;
		case 3: System.out.println("enter 2 numbers");
		a=sc.nextInt();
		b=sc.nextInt();
		System.out.println("the multiplication of the two numbers: "+(float)(a*b));
		break;
		case 4: System.out.println("enter 2 numbers");
		a=sc.nextInt();
		b=sc.nextInt();
		System.out.println("the division of the two numbers: "+(float)(a/b));
		break;
		case 5:System.exit(0);
		default:System.out.println("Invalid Input");
	}
	}
while(choice!=5);
}
}