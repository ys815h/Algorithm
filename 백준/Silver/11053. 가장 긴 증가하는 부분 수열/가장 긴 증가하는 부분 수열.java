import java.util.*;
import java.io.*;

public class Main {
	
	static Integer[] dp;
	static int[] seq;
	static Queue<Integer> q = new LinkedList<>();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		seq = new int[N];
		dp = new Integer[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i=0; i<N; i++) {
			seq[i] = Integer.parseInt(st.nextToken());
		}
		
//		0 ~ N-1까지 탐색
		for (int i=0; i<N; i++) {
			LIS(i);
		}
//		최댓값 찾기
		int max = dp[0];
		for (int i=0; i<N; i++) {
			max = Math.max(max, dp[i]);
		}
		System.out.println(max);
	}
	
	
	// Top-Down 방식
	static int LIS(int N) {
//		만약 탐색하지 않던 위치의 경우
		if(dp[N] == null) {
			dp[N] = 1;	// 1로 초기화
			
			// N-1 부터 0까지중 N보다 작은 값들을 찾으며 재귀호출
			for(int i=N-1; i>=0; i--) {
				if(seq[i] < seq[N]) {
					dp[N] = Math.max(dp[N], LIS(i)+1);
				}
			}
			
		}
		
		return dp[N];
	}
}
