class Solution {
    public double solution(int balls, int share) {
        double answer = 1;
        
        for (int i=0; i<share; i++) {
            answer = answer * (balls-i) / (i+1);
        }
        return answer;
    //     return factorial(balls) / (factorial(balls-share) * factorial(share));
    // }
    // public static double factorial(int val) {
    //     double total = 1;
    //     for(int i=1; i<=val; i++) {
    //         total *= i;
    //     }
    //     return total;
    }
}