/*
1. You are given an array(arr) of distinct integers.
2. You have to find if there are two pairs(A, B) and (C, D) present in the given array which satisfies the condition A+B = C+D.

Sample Input
8
1 2 998 72 87576 21 45 -1

Sample Output
false
*/
public static boolean solution(int[] arr) 
{
	HashSet<Integer> set = new HashSet<>();
	for(int i = 0 ; i < arr.length ; i++) 
	{
		for(int j = i + 1; j < arr.length ; j++) 
		{
			int sum = arr[i] + arr[j];
			if(set.contains(sum))
			{
				return true;
			}
			else
			{
				set.add(sum);
			}
		}
	}
	return false;
}
