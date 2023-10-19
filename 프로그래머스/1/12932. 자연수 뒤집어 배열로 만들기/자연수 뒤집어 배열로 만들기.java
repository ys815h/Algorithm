import java.util.*;

class Solution {
    public ArrayList<Long> solution(long n) {
        ArrayList<Long> answer = new ArrayList<>();
        
        while(true){
            
            if (n < 10) {
                answer.add(n);
                break;
            }
            
            answer.add((n%10));
            n = n / 10;
        }
        return answer;
    }
}