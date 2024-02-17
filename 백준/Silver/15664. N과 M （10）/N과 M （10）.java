import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int[] arr;
	static boolean[] visited;
	
	static Stack<Integer> stack = new Stack<>();
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
		
		if (stack.size() == m) {
			for(int val : stack) {
				sb.append(val + " ");
			}
			sb.append("\n");
			return;
		}
		
		int log = 0;
		for (int i=s; i<n; i++) {
			if (log != arr[i] && !visited[i]) {
				log = arr[i];
				visited[i] = true;
				stack.push(arr[i]);
				dfs(i);
				stack.pop();
				visited[i] = false;
			}
			
		}
		return;
	}
}
