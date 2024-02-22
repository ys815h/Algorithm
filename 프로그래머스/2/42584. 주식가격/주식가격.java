import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] prices) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<prices.length-1; i++) {
            int cnt = 0;
            for (int j=i+1; j<prices.length; j++) {
                cnt++;
                if (prices[i] > prices[j]) break;
            }
            answer.add(cnt);
        }
        answer.add(0);
        
        return answer;
    }
}