import java.util.Scanner;

public class Alphabetical {
    public static void main(String args[]) {
        // Creating a Scanner object to read input from the console
        Scanner scan = new Scanner(System.in);

        // Declaring an array to store 10 names
        String[] names = new String[10];

        // Prompting the user to enter 10 names
        System.out.println("Please enter 10 names ");
        for (int i = 0; i < 10; i++) {
            System.out.print("Name " + (i + 1) + ": ");
            // Reading the name input from the user and storing it in the names array
            String inputName = scan.nextLine();
            String capitalized = inputName.substring(0, 1).toUpperCase() + inputName.substring(1);
            names[i] = capitalized;
        }

        // Sorting the names array in alphabetical order
        for (int i = 0; i < names.length - 1; i++) {
            for (int j = 0; j < names.length - i - 1; j++) {
                if (names[j].compareTo(names[j + 1]) > 0) {
                    // Swap names[j] and names[j + 1]
                    String temp = names[j];
                    names[j] = names[j + 1];
                    names[j + 1] = temp;
                }
            }
        }

        // Displaying the names in alphabetical order
        System.out.println("The names in alphabetical order");
        for (String name : names) {
            System.out.println(name);
        }

        // Closing the Scanner object to prevent resource leak
        scan.close();
    }
}