class Solution 
{
    //Function to check if the linked list has a loop.
    public static boolean detectLoop(Node head)
    {
        if(head == null) return false;
        
        Node fast = head;
        Node slow = head;
        
        while(fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
            
            if(fast == slow)
                return true;
        }
		// if traversal reaches to NULL this means no cycle.
        return false;
    }
}
