import java.io.*;
import java.net.*;

public class Client{

  public static void main(String[] args){
    try{
      Socket sock = new Socket("localhost",3341);
      DataOutputStream output = new DataOutputStream(sock.getOutputStream());
      output.writeUTF("Hello");
      output.flush();
      output.close();
      sock.close();
    }catch(Exception e){
      e.printStackTrace();
    }
  }

}
