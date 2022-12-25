int kthSmallest(int arr[], int l, int r, int k) 
{
        priority_queue<int> pq;
        for (int i=r; i>=0; i--)
        {
            pq.push(arr[i]);
            if (pq.size() > k)pq.pop();
        }
        return pq.top();
}
