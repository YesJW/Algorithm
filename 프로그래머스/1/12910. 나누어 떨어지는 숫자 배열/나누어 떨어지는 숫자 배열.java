import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        
        int count = 0;
        for(int i : arr)
            if(i % divisor == 0)
                count++;
                
        if(count == 0){
            int[] answer = {-1};
            return answer;
        }
        
        int num = 0;
        int[] answer = new int[count];
        for(int i : arr)
               if(i % divisor == 0){
                   answer[num++] = i;
               }      
        Arrays.sort(answer);
        return answer;
    }
}