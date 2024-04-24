import java.util.*;

class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int[][] dxdy = {{1,0},{0,1},{-1,0},{0,-1}};
        
        for(int[] d : dxdy){
            int cx = w + d[0];
            int cy = h + d[1];
            
            if(0<=cx && cx<board.length && 0<=cy && cy<board.length){
                if(board[cy][cx].equals(board[h][w])){
                    answer+=1;
                }
            }
        }
        
        return answer;
    }
    
    
}