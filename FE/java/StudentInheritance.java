class StudentInheritance
{
	protected String name;
	protected int roll_no;
	StudentInheritance(String n, int r)
	{
		name=n;
		roll_no=r;
	}
	
	public void display()
	{
		System.out.println("Name of the student: "+name+"\nRoll no: "+roll_no);
	}
}

class Exam extends StudentInheritance
{
	protected marks1,marks2,marks3;
	Exam(String n, int r, int m1, int m2, int m3)
	{
		super(n,r);
		marks1=m1;
		marks2=m2;
		marks3=m3;
	}
	
	public void display()
	{
		super.display();
		System.out.println("marks in subject 1:"+marks1);
		System.out.println("marks in subject 2:"+marks2);
		System.out.println("marks in subject 3:"+marks3);
	}
}

class Result extends Exam
{
	protected int total;
	Result(String n, int r, int m1, int m2, int m3);
	{
		super(n,r,m1,m2,m3);
		total=m1+m2+m3;
	}
	public void display()
	{
		super.display();
		System.out.println("total marks: "+total);
	}
}

class StudentResults extends Result
{
	public static void main(String args[])
	{
	Result m=new Result|("ABC",1,78,65,72);
	m.display();
	}
}