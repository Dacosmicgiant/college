public class Student1
{
	int id, age;
	String name;
	Student1(int i, String n)
	{
	id=i;
	name=n;
	}

	Student1(int i, String n, int a)
	{
	id=i;
	name=n;
	age=a;
	}

	void display()
	{
	System.out.println(id+" "+name+" "+age);
	}

	public static void main(String args[])
	{
	Student1 s1=new Student1(427, "Kshitij");
	Student1 s2=new Student1(428, "Vedant", 18);
	s1.display();
	s2.display();
	}
}