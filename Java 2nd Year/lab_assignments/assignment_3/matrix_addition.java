import java.util.Scanner;

public class matrix_addition {
    public static void main(String[] args) {
        // Creating a Scanner object to read input from the console
        Scanner scan = new Scanner(System.in);

        // Prompting the user to enter elements for the 1st matrix
        System.out.println("Enter elements for the 1st matrix");
        int[][] matrix1 = enter_matrix(scan);

        // Prompting the user to enter elements for the 2nd matrix
        System.out.println("Enter elements for the 2nd matrix");
        int[][] matrix2 = enter_matrix(scan);

        // Adding the two matrices
        int[][] sum_matrix = add_matrix(matrix1, matrix2);
        
        // Displaying the sum of the matrices
        System.out.println("The sum of the matrices is:");
        display(sum_matrix);

        // Closing the Scanner object to prevent resource leak
        scan.close();
    }

    // Method to enter elements for a matrix
    public static int[][] enter_matrix(Scanner scan) {
        // Creating a 3x3 matrix
        int[][] matrix = new int[3][3];
        
        // Looping through rows and columns to input elements
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // Prompting the user to enter an element at a specific position
                System.out.print("Enter element at position (" + (i + 1) + "." + (j + 1) + "): ");
                matrix[i][j] = scan.nextInt();
            }
        }
        return matrix;
    } 

    // Method to add two matrices
    public static int[][] add_matrix(int[][] matrix1, int[][] matrix2) {
        // Creating a matrix to store the sum of the matrices
        int[][] sum_matrix = new int[3][3];
        
        // Looping through rows and columns to add corresponding elements of the matrices
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // Adding corresponding elements from matrix1 and matrix2 and storing the result in sum_matrix
                sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        return sum_matrix;
    }

    // Method to display a matrix
    public static void display(int[][] matrix) {
        // Looping through rows and columns to display the elements of the matrix
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // Printing each element of the matrix followed by a space
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}