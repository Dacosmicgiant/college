class A extends Thread
{
	public void run()
	{
		for(int i=1;i<=26;i++)
		{
			System.out.print(i+" ");
		try{
			Thread.sleep(500);
			}
		catch(Exception e){}
		}
	}
}

class B implements Runnable
{
	public void run()
	{
		for(int i=1;i<=26;i++)
		{
			System.out.print((char)(i+64)+" ");
		try{
			Thread.sleep(500);
			}
		catch(Exception e){}
		}
	}
}
	
class ex12
{
	public static void main(String args[])
	{
		A a= new A();
		a.start();

		B b= new B();
		Thread t=new Thread(b);
		t.start();
	}
}