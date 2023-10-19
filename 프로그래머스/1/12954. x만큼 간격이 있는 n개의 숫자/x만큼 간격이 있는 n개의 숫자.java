import java.util.*;

class Solution {
    public ArrayList<Long> solution(int x, int n) {
        ArrayList<Long> answer = new ArrayList<>();
        long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += (long)x;
            answer.add(sum);
        }
        return answer;
    }
}