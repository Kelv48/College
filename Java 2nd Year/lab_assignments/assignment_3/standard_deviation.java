import java.util.Scanner;

public class standard_deviation {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        
        // Prompting the user to enter a real number
        System.out.println("Please enter a Real number ");
        int N = scan.nextInt();
        
        // Creating an array to store N numbers
        double[] array = new double[N];

        // Looping to input N numbers
        for (int i = 0; i < N; i++) {
            // Prompting the user to enter each value
            System.out.println("Please enter value #" + (i + 1) + ": ");
            array[i] = scan.nextDouble();
        }

        // Calculating the standard deviation of the entered numbers
        double StdDev = calcStdDev(array);
        
        // Displaying the calculated standard deviation
        System.out.println("The Standard deviation of N numbers is " + StdDev);

        // Closing the Scanner object to prevent resource leak
        scan.close();
    }

    // Method to calculate the standard deviation
    public static double calcStdDev(double[] array) {
        double mean = calcmean(array);
        
        // Variable to store the sum of squared differences
        double sumOfSquaredDifferences = 0;

        for (double value : array) {
            sumOfSquaredDifferences += Math.pow(value - mean, 2);
        }

        // Calculating the standard deviation using the formula
        double std = sumOfSquaredDifferences / (array.length - 1);
        
        return Math.sqrt(std);
    }

    // Method to calculate the mean of an array
    public static double calcmean(double[] array) {
        // Calculating the sum of all elements in the array
        double sum = 0.0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }
        // Calculating the mean by dividing the sum by the number of elements
        return sum / array.length;
    }
}
