import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        Queue<Integer> p_q = new LinkedList<>();
        Queue<Integer> s_q = new LinkedList<>();
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<speeds.length; i++) {
            p_q.offer(progresses[i]);
            s_q.offer(speeds[i]);
        }
        int cnt = 0;
        int day = 1;
        while (!p_q.isEmpty()) {
            while(p_q.peek() + s_q.peek() * day >= 100) {
                p_q.poll();
                s_q.poll();
                cnt++;
                if (p_q.isEmpty()) break;
            }
            if(cnt > 0) {
                answer.add(cnt);
                cnt = 0;
            }
            day++;
        }
        return answer;
    }
}