import java.util.*;
import java.io.*;

public class Main {
	
	static StringBuilder sb = new StringBuilder();
	static boolean[] visited;
	static int[][] arr;
	
	static int node, line, start;
	static Queue<Integer> q = new LinkedList<>();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		node = Integer.parseInt(st.nextToken());
		line = Integer.parseInt(st.nextToken());
		start = Integer.parseInt(st.nextToken());
		
		arr = new int[node+1][node+1];
		visited = new boolean[node+1];
		
		for (int i=1; i<=line; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			
			int s = Integer.parseInt(st.nextToken());
			int e = Integer.parseInt(st.nextToken());
			
			// python으로 할 때 하던 방식
			arr[s][e] = e;
			arr[e][s] = s;
//			arr[s][e] = arr[e][s] = 1;
			
		}
		dfs(start);
		sb.append("\n");
		visited = new boolean[node+1];
		bfs(start);
		System.out.println(sb);
	}
	
	public static void dfs(int start) {
		visited[start] = true;
		sb.append(start + " ");
		
		// python으로 풀 때 하던 방식
		for (int val : arr[start]) {
			if(val != 0 && !visited[val]) {
				visited[val] = true;
				dfs(val);
			}
		}
		
//		for(int i=1; i<=node; i++) {
//			if(arr[start][i] == i && !visited[i]) {
//				visited[i] = true;
//				dfs(i);
//			}
//		}

	}
	
	public static void bfs(int start) {
		q.add(start);
		visited[start] = true;
		
		while(!q.isEmpty()) {
			start = q.poll();
			sb.append(start + " ");
			
			// python으로 풀 때 하던 방식
			for (int val : arr[start]) {
				if(val != 0 && !visited[val]) {
					visited[val] = true;
					q.offer(val);
				}
			}
			
			
//			for (int i=1; i<=node; i++) {
//				if(arr[start][i] == 1 && !visited[i]) {
//					visited[i] = true;
//					q.offer(i);
//				}
//			}
		}
	}
	
	

}
