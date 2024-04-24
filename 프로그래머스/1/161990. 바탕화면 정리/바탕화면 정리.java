import java.util.*;
class Solution {
    public int[] solution(String[] wallpaper) {
        
        int x1,y1,x2,y2;
        x1 = 9999;
        x2 = 0;
        y1 = 9999;
        y2 = 0;
        
        for(int i = 0; i < wallpaper.length; i++){
            for(int j = 0; j < wallpaper[0].length(); j++){
                if(wallpaper[i].charAt(j) == '#'){
                    if(x1 > j)
                        x1 = j;
                    if(x2 < j)
                        x2 = j;
                    if(y1 > i)
                        y1 = i;
                    if(y2 < i)
                        y2 = i;
                }
            }
        }
        int[] answer = {y1,x1,y2+1,x2+1};

        return answer;
    }
}