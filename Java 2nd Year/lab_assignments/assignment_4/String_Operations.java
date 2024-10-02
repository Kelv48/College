import java.util.Scanner;

public class String_Operations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input two strings from the user
        System.out.println("Enter the first string:");
        String str1 = scanner.nextLine().trim(); // Trim to remove leading and trailing spaces

        System.out.println("Enter the second string:");
        String str2 = scanner.nextLine().trim(); // Trim to remove leading and trailing spaces

        // Concatenate the strings
        String concatenatedString = str1 + str2;
        System.out.println("Concatenated string: " + concatenatedString);

        // Count number of characters excluding spaces
        int charCount = concatenatedString.replaceAll("\\s", "").length();
        System.out.println("Number of characters (excluding spaces): " + charCount);

        // Print concatenated string in reverse order
        System.out.print("Concatenated string in reverse order: ");
        for (int i = concatenatedString.length() - 1; i >= 0; i--) {
            System.out.print(concatenatedString.charAt(i));
        }
        System.out.println();

        // Print characters that occur twice
        System.out.print("Characters occurring twice: ");
        String duplicates = Find_Duplicates(concatenatedString);
        if (duplicates.isEmpty()) {
            System.out.println("None");
        } else {
            System.out.println(duplicates);
        }

        scanner.close();
    }

    // Method to find characters that occur twice in a string
    private static String Find_Duplicates(String str) {
        StringBuilder duplicates = new StringBuilder();
        int[] count = new int[256]; // Assuming ASCII characters

        // Count occurrences of each character
        for (int i = 0; i < str.length(); i++) {
            count[str.charAt(i)]++;
        }

        // Add characters occurring twice to the result
        for (int i = 0; i < 256; i++) {
            if (count[i] > 1) {
                duplicates.append((char) i);
            }
        }

        return duplicates.toString();
    }
}