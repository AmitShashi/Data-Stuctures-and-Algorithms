//Stack using queue 
class Queues
{
    Queue<Integer> q1 = new LinkedList<Integer>();
    
    //Function to push an element into stack using single queue
    void push(int a)
    {
	    q1.add(a);
	    
	    for(int i=0; i<q1.size()-1; i++)
	        q1.add(q1.remove());
    }  
    //Function to pop an element from stack using single queue
    int pop()
    {
	    if(q1.isEmpty()==true)  {return -1;}
	    
	    return q1.remove();
    }
}
