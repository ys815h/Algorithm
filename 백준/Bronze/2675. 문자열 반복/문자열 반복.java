import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int t = Integer.parseInt(br.readLine());
		for (int i=0; i<t; i++) {

//			String[] arr = br.readLine().split(" ");	// 공백 분리
//			
//			int t2 = Integer.parseInt(arr[0]);	// String -> int
//			String str = arr[1];
//			nextToken이 아닌 배열로 담아 새 변수 선언해서 사용
			
			st = new StringTokenizer(br.readLine(), " ");
			
			int t2 = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			
			for (int j=0; j<str.length(); j++) {
				for (int k=0; k<t2; k++) {
					bw.write(str.charAt(j));
				}
				
			}
			bw.write("\n");
		}
		
		bw.close();
		
	}


}
