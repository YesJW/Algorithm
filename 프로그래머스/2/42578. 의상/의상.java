import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hmap = new HashMap<String, Integer>();
        for(int i = 0; i < clothes.length; i++){
            hmap.put(clothes[i][1].toString(),hmap.getOrDefault(clothes[i][1].toString(), 1) + 1);
        }
        
        for(int i : hmap.values()){
            answer *= i;
        }
        
        return answer-1;
    }
}