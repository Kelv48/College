import java.util.Scanner;
public class transpose_matrix {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input for the matrix
        System.out.println("Enter the number of rows:");
        int rows = scanner.nextInt();
        System.out.println("Enter the number of columns:");
        int columns = scanner.nextInt();
        int[][] matrix = new int[rows][columns];

        // Input elements of the matrix
        System.out.println("Enter elements of the matrix:");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print("Enter element at position (" + (i + 1) + "," + (j + 1) + "): ");
                matrix[i][j] = scanner.nextInt();
            }
        }

        // Display original matrix
        System.out.println("\nOriginal matrix:");
        displayMatrix(matrix);

        // Transpose the matrix
        int[][] transposeMatrix = transpose(matrix);

        // Display transpose matrix
        System.out.println("\nTranspose matrix:");
        displayMatrix(transposeMatrix);

        scanner.close();
    }

    // Method to compute transpose of a matrix
    public static int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;

        int[][] transposeMatrix = new int[columns][rows];

        for (int i = 0; i < columns; i++) {
            for (int j = 0; j < rows; j++) {
                transposeMatrix[i][j] = matrix[j][i];
            }
        }

        return transposeMatrix;
    }

    // This method displays the matrix
    public static void displayMatrix(int[][] matrix) {
        int rows = matrix.length;
        int columns = matrix[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}