import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        Queue<Integer> p_q = new LinkedList<>();
        Queue<Integer> m_q = new LinkedList<>();
        int[] max = Arrays.copyOf(priorities, priorities.length);
        Arrays.sort(max);
        
        for(int i=0; i<priorities.length; i++) {
            p_q.offer(priorities[i]);
        }
        for(int i=max.length-1; i>=0; i--) {
            m_q.offer(max[i]);
        }
        
        while(!p_q.isEmpty()) {
            if(p_q.peek() == m_q.peek() && location == 0) break;
            else {
                // 우선순위 높은 프로세스일 때
                if(p_q.peek() == m_q.peek()) {
                    p_q.poll();
                    m_q.poll();
                    answer++;
                } else {
                    p_q.offer(p_q.poll());
                }
                if(location == 0) {
                    location = p_q.size()-1;
                } else {
                    location--;
                }
            }
        }
        
        return answer;
    }
}