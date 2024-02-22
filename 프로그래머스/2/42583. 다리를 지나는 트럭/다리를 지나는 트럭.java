import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> t_q = new LinkedList<>();
        // 다리크기가 bridge_length인 다리List b_q
        Queue<Integer> b_q = new LinkedList<>();
        int total = 0;
        
        for (int i=0; i<truck_weights.length; i++) {
            t_q.offer(truck_weights[i]);
        }
        for (int i=0; i<bridge_length; i++) {
            b_q.offer(0);
        }
        
        while(!t_q.isEmpty()) {
            answer++;
            total -= b_q.poll();
            if (total + t_q.peek() <= weight) {
                total += t_q.peek();
                b_q.offer(t_q.poll());
            } else {
                b_q.offer(0);
            }
        }
//         마지막 대기트럭이 다리위에 올랐기 때문에 다리길이만큼 더해주면 끝
        answer += bridge_length;
        return answer;
    }
}