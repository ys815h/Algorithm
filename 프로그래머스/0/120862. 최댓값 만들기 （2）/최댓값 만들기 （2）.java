class Solution {
    public int solution(int[] numbers) {
        int answer = numbers[0] * numbers[1];
        // int temp = 0;
        
        for (int i=0; i<numbers.length; i++) {
            int x = numbers[i];
            for (int j=0; j<numbers.length; j++) {
                int y = numbers[j];
                if (x == y) continue;
                else if (x > 0 && y > 0) {
                    answer = x*y > answer ? x*y : answer;
                } else if(x < 0 && y < 0) {
                    answer = x*y > answer ? x*y : answer;
                }
                
            }
            
        }
        
        return answer;
    }
}