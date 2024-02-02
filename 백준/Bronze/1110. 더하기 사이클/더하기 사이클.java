//0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.

//먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
//그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

//26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
//위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
//N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.


//첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int start = Integer.parseInt(br.readLine());
//		int count = 1;
//		int sum = 0;
//		int cycle = 0;
//		sum = start%10 + start/10;
//		cycle = (start%10)*10 + sum%10;
		
//		while (cycle != start) {
//			count++;
//			sum = cycle%10 + cycle/10;
//			cycle = (cycle%10)*10 + sum%10;
//		}
//		
//		bw.write(count + "\n");
	
		bw.write(DFS(1, (start%10)*10 + (start%10+start/10)%10, start) + "\n");
		bw.close();
	}
	
	public static int DFS(int cnt, int cycle, int ans) {
		if (ans == cycle) {
			return cnt;
		} else {
			cycle = (cycle%10)*10 + (cycle%10 + cycle/10)%10;
			cnt++;
		}
		return DFS(cnt, cycle, ans);
	}
}
