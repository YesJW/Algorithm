import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int front = 0;
        int back = people.length-1;
        
        while(front < back){
            if(people[back] + people[front] > limit){
                answer += 1;
                back -= 1;
            }
            else{
                back -=1;
                front +=1;
                answer += 1;
            }
            if(front == back){
                answer += 1;
                break;
            }
            
        }
        return answer;
    }
}