import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        
        for(int i = 0; i < want.length; i++){
            map.put(want[i], number[i]);
        }
        
        for(int i = 0; i < discount.length - 9; i++){
            boolean check = true;
            HashMap<String, Integer> hmap = new HashMap<String, Integer>();
            for(int j = i; j < i+10; j++){
                hmap.put(discount[j], hmap.getOrDefault(discount[j], 0) + 1);

            }
            for(String key : map.keySet()){
                
                if(map.get(key) != hmap.get(key)){
                    check = false;
                    break;
                }
            }
            if(check)
                answer += 1;
        }
        return answer;
    }
}