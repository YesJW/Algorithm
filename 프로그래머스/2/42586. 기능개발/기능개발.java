import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int time = 1;
        int now = 0;
        int count = 0;
        
        List<Integer> arr = new ArrayList<>();
        
        while(now < progresses.length){
            if(progresses[now] + speeds[now] * time >= 100){
                now += 1;
                count += 1;
            }
            else{
                if(count >= 1){
                    arr.add(count);                    
                    count = 0;
                }
                
                time += 1;
            }
            if(now == progresses.length)
                arr.add(count);
        }
        int[] answer = new int[arr.size()];
        
        for(int i = 0; i < arr.size(); i++){
            answer[i] = arr.get(i);
        }
        
        return answer;
    }
}