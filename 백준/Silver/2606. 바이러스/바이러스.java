import java.util.*;
import java.io.*;

public class Main {
	static int node, line, s, e, start, cnt;
	static int[][] graph;
	static boolean[] visited;
	static Queue<Integer> q = new LinkedList<>();
	
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
//		dfs(start);
//		System.out.println("dfs풀이법");
//		System.out.println(cnt);
//		visited = new boolean[node + 1];
//		cnt = 0;
		bfs(start);
//		System.out.println("bfs풀이법");
		System.out.println(cnt);
	}
	public static void dfs(int s) {
		visited[s] = true;
		for (int i=1; i<=node; i++) {
			if(graph[s][i] != 0 && !visited[i]) {
				cnt ++;
				dfs(i);
			}
		}
	}
	public static void bfs(int s) {
		visited[s] = true;
		q.offer(s);
		
		while(!q.isEmpty()) {
			start = q.poll();
			
			for (int i=1; i<=node; i++) {
				if(graph[start][i] != 0 && !visited[i]) {
					cnt++;
					visited[i] = true;
					q.offer(i);
				}
			}
		}
	}
	
}
