import java.util.*;

class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        
        for(int val : array) {
            answer += val > height ? 1 : 0;
        }
        return answer;
    }
}