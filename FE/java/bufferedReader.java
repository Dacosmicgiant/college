import java.io.*;

class bufferedReader
{

	public static void main(String[] args)throws Exception
	{
	BufferedReader b = new BufferedReader(new InputStreamReader(System.in));
	System.out.println("enter a string");
	String s=b.readLine();
	System.out.println("the entered string is:"+s);
	System.out.println("enter your roll number");
	int rno=Integer.parseInt(b.readLine());
	System.out.println("your rno is: "+rno);
	}
}