import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        
        List<Integer> arr = new ArrayList<Integer>();
        
        for(int i = 0; i < numbers.length; i++){
            for(int j = i+1; j < numbers.length; j++){
                if(!(arr.contains(numbers[i] + numbers[j]))){
                    arr.add(numbers[i] + numbers[j]);
                }
            }
        }
        int [] answer = arr.stream().mapToInt(i -> i).toArray();
        Arrays.sort(answer);
        
        
        return answer;
    }
}