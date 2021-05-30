import java.io.*;
import java.net.*;

class TCPClient {
    public static void main(String[] args){
        String sentence;
        String modifiedSentence;
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        Socket clientSocket = new Socket("localhost", 1234);
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        sentence = inFromUser.readline();
        outToServer.writeBytes(sentence + '\n');
        modifiedSentence = inFromServer.readline();
        System.out.println("REPLY FROM SERVER : " + modifiedSentence);
        clientSocket.close();    
    }
}