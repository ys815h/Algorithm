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
			
			String[] arr = br.readLine().split("");
			int score = 0;
			int cnt = 1;
			for (String val : arr) {
				if (val.equals("O")) {
					score += cnt;
				} else {
					cnt = 0;
				}
				cnt++;
			}
			bw.write(score + "\n");
		}
		bw.close();
	}
}
