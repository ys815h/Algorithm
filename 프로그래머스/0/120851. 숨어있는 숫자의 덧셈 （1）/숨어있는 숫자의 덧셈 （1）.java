class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] arr = my_string.split("");
        
        for (int i=0; i<arr.length; i++) {
            try {
                answer += Integer.parseInt(arr[i]);
            } catch (Exception e) {}
            
        }
        
        return answer;
    }
}