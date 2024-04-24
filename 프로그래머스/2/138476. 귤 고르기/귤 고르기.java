import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int count = 0;
        int sum = 0;
        
        HashMap<Integer, Integer> hmap = new HashMap<>();
        for(int i : tangerine)
            hmap.put(i, hmap.getOrDefault(i, 0) + 1);
        
        List<Integer> arr = new ArrayList<>(hmap.values());
        Collections.sort(arr, Collections.reverseOrder());
        
        for(int i : arr){
            if(sum + i >= k){
                count++;
                break;
            }
            else{
                sum += i;
                count++;
            }
        }
        
        return count;
    }
}