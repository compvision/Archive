import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class client {
	public static void main(String [] args) {
		try {
			Socket s = new Socket("localhost", 3341);
			BufferedReader input = new BufferedReader(new InputStreamReader(s.getInputStream()));
			PrintWriter output = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
			output.println("whatsup diggity dogs");
			output.flush();
			output.close();
			input.close();
			s.close();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
}