import java.util.Scanner;

public class even_or_odd {
    public static void main(String args[]) {
        // Creating a Scanner object to read input from the console
        Scanner scan = new Scanner(System.in);
        
        // Declaring an array to store 10 numbers
        int[] numbers = new int[10];

        // Prompting the user to enter 10 numbers
        for (int i = 0; i < 10; i++) {
            System.out.println("Please enter a number ");
            // Reading the number input from the user and storing it in the numbers array
            numbers[i] = scan.nextInt();
        }

        // Closing the Scanner object to prevent resource leak
        scan.close();
        
        // Calling the checkNum method to count even and odd numbers
        checkNum(numbers);
    } 

    // Method to check whether each number in the array is even or odd
    private static void checkNum(int[] numbers) {
        // Variables to store the counts of even and odd numbers
        int even = 0;
        int odd = 0;
        
        // Iterating through the numbers array
        for (int i = 0; i < numbers.length; i++) {
            // Checking if the current number is even
            if (numbers[i] % 2 == 0) {
                even += 1; // Incrementing the count of even numbers
            } else {
                odd += 1; // Incrementing the count of odd numbers
            }
        }
        
        // Displaying the count of even and odd numbers
        System.out.println("There were " + even + " even numbers");
        System.out.println("There were " + odd + " odd numbers");
    }
}