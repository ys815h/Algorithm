import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int[] arr;
	static boolean[] visited;
	static Stack<Integer> st = new Stack<>();
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		arr = new int[n];
		visited = new boolean[n];
		
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		
		dfs(0);
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
		
		for(int i=s; i<n; i++) {
			if(!visited[i]) {
				visited[i] = true;
				st.push(arr[i]);
				dfs(i);
				st.pop();
				visited[i] = false;
			}
		}
		return;
	}
}
