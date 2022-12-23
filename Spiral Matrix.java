/*
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
*/

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        List<Integer> res = new ArrayList<Integer>();
        
        if (matrix.length == 0) {
            return res;
        }
        
        int top = 0; //row begin
        int bottom = matrix.length-1; //row end
        int left = 0; // column begin
        int right = matrix[0].length - 1; //column end
        
        while (top <= bottom && left <= right) {
            // Traverse Right
            for (int j = left; j <= right; j ++) {
                res.add(matrix[top][j]);
            }
            top++;
            
            // Traverse Down
            for (int j = top; j <= bottom; j ++) {
                res.add(matrix[j][right]);
            }
            right--;
            
            if (top <= bottom) {
                // Traverse Left
                for (int j = right; j >= left; j --) {
                    res.add(matrix[bottom][j]);
                }
            }
            bottom--;
            
            if (left <= right) {
                // Traver Up
                for (int j = bottom; j >= top; j --) {
                    res.add(matrix[j][left]);
                }
            }
            left ++;
        }
        
        return res;
    }
}
