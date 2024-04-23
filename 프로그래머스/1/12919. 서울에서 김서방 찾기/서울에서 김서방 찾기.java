import java.util.Arrays;
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int num = Arrays.asList(seoul).indexOf("Kim");
        answer = "김서방은 "+num+"에 있다";
        return answer;
    }
}