
class Solution {
    public int solution(int n) {
        int answer = 0;
        int temp = 0;
        
        temp = (int)Math.sqrt(n);
        if (n == (int)Math.pow(temp, 2)) {
            answer = 1;
        } else {
            answer = 2;
        }
        return answer;
    }
}