import java.util.*;
import java.io.*;

public class Main {
	
	static int[][] map;
	static boolean[][] visited;
	static int n, m;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {-1, 0, 1, 0};
	
	static Queue<int[]> q = new LinkedList<>();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		for(int i=0; i<n; i++){
            String s = br.readLine();
            for(int j=0; j<m; j++){
                map[i][j] = s.charAt(j) - '0';
            }
        }
//		for (int i=0; i<n; i++) {
//			String[] line = br.readLine().split("");
//			for(int j=0; j<m; j++) {
//				map[i][j] = Integer.parseInt(line[j]);
//			}
//		}
		visited = new boolean[n][m];
		bfs(0, 0);
		System.out.println(map[n-1][m-1]);
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
				if (nx>=0 && nx<m && ny>=0 && ny<n) {
					
					// 이동한 지점이 벽이 아닐 경우
					if (map[ny][nx] != 0 && !visited[ny][nx]) {
						visited[ny][nx] = true;
						map[ny][nx] = map[y][x] + 1;
						q.offer(new int[] {nx, ny});
					}
				}
			}
			
			
		}
	}
}
