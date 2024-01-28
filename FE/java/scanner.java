import java.util.*;
import java.util.Scanner;

public class scanner
{
	public static void main(String[] args)throws Exception
	{
		Scanner s1=new Scanner(System.in);
		System.out.println("enter a string");
		String s=s1.nextLine();
		System.out.println("enter a character");
		char c=(char)System.in.read();
		System.out.println("Enter a byte");
		byte b=s1.nextByte();
		System.out.println("enter an integer");
		int i=s1.nextInt();
		System.out.println("enter a short");
		short sh=s1.nextShort();
		System.out.println("enter a float");
		float f=s1.nextFloat();
		System.out.println(""+s+c+b+i+sh+f);
	}
}