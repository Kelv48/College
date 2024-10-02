import java.io.*;

public class file_reader {
    // Main driver method
    public static void main(String[] args) throws Exception {
        // Passing the path to the file as a parameter
        FileReader fr = new FileReader(
                "C:\\Users\\UCC\\Desktop\\test.txt");
        // Declaring loop variable
        int i;
        // Holds true till there is nothing to read
        while ((i = fr.read()) != -1)
            // Print all the content of a file
            System.out.print((char) i);
        fr.close();
    }
}
