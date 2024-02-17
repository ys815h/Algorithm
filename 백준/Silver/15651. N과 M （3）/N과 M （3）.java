import java.util.*;
import java.io.*;

public class Main {
	static int n, m, s;
	static int[] graph;
	static Stack<Integer> st = new Stack<>();
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(token.nextToken());
		m = Integer.parseInt(token.nextToken());
		dfs(1);
		System.out.println(sb);
		
			
	}
	public static void dfs(int s) {
		if (st.size() == m) {
			for(int val : st) {
				sb.append(val + " ");
			}
			sb.append("\n");
			return;
		}
		for (int i=1; i<=n; i++) {
			st.push(i);
			dfs(i);
			st.pop();
		}
		return;
	}
	
}
