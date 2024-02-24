// 문제를 찍는 순서가 있음
// 수포자1 : 1, 2, 3, 4, 5, ~
// 수포자2 : 2, 1, 2, 3, 2, 4, 2, 5, ~
// 수포자3 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ~
import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        int [] stu1ans = {1, 2, 3, 4, 5};
        int [] stu2ans = {2, 1, 2, 3, 2, 4, 2, 5};
        int [] stu3ans = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int stu1 = 0;
        int stu2 = 0;
        int stu3 = 0;
        for (int i = 0; i < answers.length; i++) {
            int ans = answers[i];
            if (stu1ans[i % stu1ans.length] == ans) {
                stu1++;
            }
            if (stu2ans[i % stu2ans.length] == ans) {
                stu2++;
            }
            if (stu3ans[i % stu3ans.length] == ans) {
                stu3++;
            }
        }
        ArrayList<Integer> answer = new ArrayList<>();
        if (stu1 == stu2) {
            if (stu2 == stu3) {
                answer.add(1);
                answer.add(2);
                answer.add(3);
            } else if(stu2 < stu3) {
                answer.add(3);
            } else {
                answer.add(1);
                answer.add(2);
            }
            
        } else if (stu1 < stu2) {
            if (stu2 == stu3) {
                answer.add(2);
                answer.add(3);
            } else if (stu2 < stu3) {
                answer.add(3);
            } else {
                answer.add(2);
            }
            
        } else {
            if (stu1 == stu3) {
                answer.add(1);
                answer.add(3);
            } else if (stu1 < stu3) {
                answer.add(3);
            } else {
                answer.add(1);
            }
        }
        return answer;
        
    }
    
}