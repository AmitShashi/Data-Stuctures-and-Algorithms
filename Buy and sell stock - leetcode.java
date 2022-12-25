
/*Best Time to Buy and Sell Stock - LEETCODE*/

class Solution 
{
    public int maxProfit(int[] A) 
    {
        int minPrice = A[0];
        int maxProfit = 0;
        for(int i=1; i<A.length; i++)
        {
            minPrice = Math.min(minPrice , A[i]);
            int curProfit = A[i]- minPrice;
            maxProfit = Math.max(curProfit,maxProfit);

        }
        return maxProfit;
    }
}
