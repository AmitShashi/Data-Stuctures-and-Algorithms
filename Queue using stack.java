//Queue using two Stacks
class StackQueue
{
    Stack<Integer> s1 = new Stack<Integer>();
    Stack<Integer> s2 = new Stack<Integer>();

    //Function to push an element in queue by using 2 stacks.
    void Push(int x)
    {
	   // Your code here
	   while(s2.isEmpty()==false)
	   {
	       s1.push(s2.pop());
	   }
	   s1.push(x);
    }
	
    
    //Function to pop an element from queue by using 2 stacks.
    int Pop()
    {
	   // Your code here
	   while(s1.isEmpty()==false)
	   {
	       s2.push(s1.pop());
	   }
	   
	   if(s2.isEmpty()==true) {return -1;}
	   
	   return s2.pop();
    }
}
