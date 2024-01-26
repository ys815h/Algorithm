class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        
        for (int val : array) {
            if (val == n) answer ++;
        }
        return answer;
    }
}