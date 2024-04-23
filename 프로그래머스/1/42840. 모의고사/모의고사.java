import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] fir = {1,2,3,4,5};
        int[] sec = {2,1,2,3,2,4,2,5};
        int[] thr = {3,3,1,1,2,2,4,4,5,5};
        int[] arr = {0,0,0};
        int now = 0;
        for(int i : answers){
            if(fir[now % fir.length] == i)
                ++arr[0];
            if(sec[now % sec.length] == i)
                ++arr[1];
            if(thr[now % thr.length] == i)
                ++arr[2];
            now++;
        }
        
        int max = Arrays.stream(arr).max().getAsInt();
        
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < 3; i++){
            if(max == arr[i])
                ans.add(i+1);
        }
        
        int[] answer = new int[ans.size()];
        for(int i = 0; i < ans.size(); i++)
            answer[i] = ans.get(i);
        
        return answer;
    }
}