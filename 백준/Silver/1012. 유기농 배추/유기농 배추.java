import java.util.*;
import java.io.*;

public class Main {
	
	static int[][] map;
	static int t, n, m, k, cnt;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {-1, 0, 1, 0};
	static boolean[][] visited;
	static Queue<int[]> q = new LinkedList<>();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		t = Integer.parseInt(br.readLine());
		for (int i=0; i<t; i++) {
			cnt = 0;
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			map = new int[m][n];
			visited = new boolean[m][n];
			
			for (int j=0; j<k; j++) {
				st = new StringTokenizer(br.readLine(), " ");
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				map[b][a] = 1;
			}
			for (int y=0; y<m; y++) {
				for(int x=0; x<n; x++) {
					if (map[y][x] == 1 && !visited[y][x]) {
						bfs(x, y);
					}
				}
			}
			System.out.println(cnt);
		}
	}
	
	public static void bfs(int x, int y) {
		q.offer(new int[] {x, y});
		visited[y][x] = true;
		
		while(!q.isEmpty()) {
			int xy[] = q.poll();
			x = xy[0];
			y = xy[1];
			
			for (int i=0; i<4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				
				// 맵 길이 안에서 움직일 때의 조건
				if (nx>=0 && nx<n && ny>=0 && ny<m) {
					
					// 이동한 지점이 벽이 아닐 경우
					if (map[ny][nx] != 0 && !visited[ny][nx]) {
						visited[ny][nx] = true;
						q.offer(new int[] {nx, ny});
					}
				}
			}
			
			
		}
		cnt++;
	}
}
