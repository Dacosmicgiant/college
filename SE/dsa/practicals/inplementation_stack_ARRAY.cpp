#include <stdio.h>
#include <conio.h>
#include <stdbool.h>

int top=-1,i;
int stack[10];
int data;
char ch;

bool isFull()
{
if(top==10/*(maxsize)*/-1)
return true;
else
return false;

}

bool isEmpty()
{
if(top==-1)
return true;
else
return false;

}

void push(int data)
{
if(!isFull())
{
top++;
stack[top]=data;

}

else{
printf("cannot insert data, stack is full\n");

}

}

int pop(){
int data;
if(!isEmpty()){
data=stack[top];
top--;
return data;

}
else{
printf("Cannot retrieve data, stack is empty.");
}
}

int peek()
{
return stack[top];
}

void show()
{
for(i=top;i>=0;i--)
{
printf("%d\n", stack[i]);
}
if(isEmpty()){
printf("Stack is empty");

}

}

int main()
{
printf("Hello user\n What would you like to do?\n");

while(ch!=7)
{

printf("1:push\n2:pop\n3:isfull?\n4:isEmpty?\n5:peek\n6:show\n7:exit");

scanf("%d",&ch);

switch(ch)
{
case 1:
{
printf("enter data element");
scanf("%d",&data);
push(data);
break;
}
case 2:
{
pop();
break;
}
case 3:
{
if(isFull()==true)
printf("Stack is full");
else
printf("not full");
break;
}
case 4:
{
if(isEmpty()==true)
printf("Stack is empty");
else
printf("Stack not empty");
break;
}
case 5:
{
peek();
break;
}
case 6:
{
show();
break;
}
}
}
getch();
}
