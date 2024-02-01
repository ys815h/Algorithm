class Solution {
    public int solution(int n) {
        int answer = 0;
        int count = 1;
        
        if ( n <= 6 && 6 % n == 0) {
            answer = count;
        } else {
            while (6*count % n != 0) {
                count++;
            }
            answer = count;
        }
        return answer;
    }
}