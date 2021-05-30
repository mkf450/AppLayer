import java.io.*;
import java.net.*;

class UDPServer {
    public static void main(String[] args){
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        DatagramSocket clientSocket = DatagramSocket();
        System.out.println("Type your message: ");
        InetAddress IPAddress = InetAddress.getByName("localhost");

        byte[] sendData = new byte[1024];
        byte[] receiveData = new byte[1024];
        
        String sentence = inFromUser.readline();
        sendData = sentence.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length(), IPAddress, 4321);
        clientSocket.send(sendPacket);
        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length());
        clientSocket.receive(receivePacket);
        String modifiedSentence = new String(receivePacket.getData());
        System.out.println("From server: "+ modifiedSentence);
        clientSocket.close();
    }
}