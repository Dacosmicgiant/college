
import java.applet.*;
import java.awt.*;

//<applet code="ex13.class" width=400 height=400> <param name="t1" value="Welcome"> </applet>

public class ex13 extends Applet
{
	String s;
	public void init()
	{
		s=getParameter("t1");
	}
	public void paint(Graphics g)
	{
	g.drawString(s,20,20);
	g.setColor(Color.YELLOW);
	g.fillOval(50,50,300,300);
	g.setColor(Color.BLACK);
	g.fillOval(100,100,30,60);
	g.setColor(Color.BLACK);
	g.fillOval(270,100,30,60);
	g.drawArc(150,210,160,80,180,180);
	}
}

//javac ex13.java
//appletviewer ex13.java