class Solution {
    public int[] solution(int n) {
        int num = 0;
        num = n%2 == 0 ? n/2 : n/2+1;
        int[] answer = new int[num];
        
        for (int i=0; i<num; i++) {
            answer[i] = i*2+1;
        }
        
        return answer;
    }
}