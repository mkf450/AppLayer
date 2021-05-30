import java.io.*;
import java.net.*;

class TCPServer {
    public static void main(String[] args){
        String clientSentence;
        String capitalizedSentence;
        ServerSocket welcomeSocket = new ServerSocket(1234);
        System.out.println("Server is listening on port 1234");
        while(true){
            Socket connectionSocket = welcomeSocket.accept();
            BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
            DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
            capitalizedSentence = clientSentence.toUpperCase()+ '\n';
            outToClient.writeBytes(capitalizedSentence); 
        } 
    }
}