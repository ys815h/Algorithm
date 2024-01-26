class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] strArr = my_string.split("");
        for (int i=0; i<strArr.length; i++) {
            for (int j=0; j<n; j++) {
                answer += strArr[i];
            }
        }
        
        return answer;
    }
}