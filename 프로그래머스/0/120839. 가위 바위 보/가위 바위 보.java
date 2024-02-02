class Solution {
    public String solution(String rsp) {
        String answer = "";
        String[] list = rsp.split("");
        
        for(String val : list) {
            if (val.equals("0")) {
                answer += "5";
            } else if(val.equals("2")) {
                answer += "0";
            } else {
                answer += "2";
            }
        }
        return answer;
    }
}