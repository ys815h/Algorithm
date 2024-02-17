import java.util.*;
import java.io.*;

public class Main {
	
	static StringBuilder sb = new StringBuilder();
	static int node, line, s, e, start, cnt;
	static int[][] graph;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		node = Integer.parseInt(br.readLine());
		line = Integer.parseInt(br.readLine());
		graph = new int[node+1][node+1];
		visited = new boolean[node+1];
		start = 1;
		cnt = 0;
		
		for(int i=1; i<=line; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			graph[s][e] = e;
			graph[e][s] = s;
		}
		dfs(start);
		System.out.println(cnt);
	}
	public static void dfs(int s) {
		visited[s] = true;
		for (int i=1; i<=node; i++) {
			if(graph[s][i] != 0 && !visited[i]) {
				cnt ++;
				visited[i] = true;
				dfs(i);
			}
			
		}
		
		
	}
	
}