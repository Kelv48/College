import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class write_string {
    public static void main(String[] args)
    throws IOException {
        String text = "This is UCC";
        Path fileName = Path.of("/USERS/UCC/Desktop/demo.docx");

        Files.writeString(fileName, text);

        String file_content = Files.readString(fileName);

        System.out.println(file_content);
    }
}