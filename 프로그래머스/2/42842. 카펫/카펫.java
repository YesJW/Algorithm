class Solution {
    public int[] solution(int brown, int yellow) {
        int sum = brown + yellow;
        int w = 0;
        int h = 0;
        for(int i = 2; i < sum; i++){
            if(sum % i == 0){
                w = sum / i;
                h = i;
                if(w*2 + h*2 - 4 == brown){
                    break;
                }
            }
        }
        int[] answer = {w,h};
        return answer;
    }
}