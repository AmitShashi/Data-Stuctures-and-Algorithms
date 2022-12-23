class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        maxsum=sum(Arr[:K])
        currsum=sum(Arr[:K])
        for i in range(K,N):
            currsum=currsum-Arr[i-K]+Arr[i]
            maxsum=max(currsum,maxsum)
        return max(currsum,maxsum)
