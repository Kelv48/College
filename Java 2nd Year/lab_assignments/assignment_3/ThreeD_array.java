import java.util.Scanner;

public class ThreeD_array {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Create and display the 3D array
        int[][][] array3D = create3DArray();
        System.out.println("3D Array:");
        display3DArray(array3D);

        // Input a number from the user
        System.out.print("\nEnter a number to search in the array: ");
        int to_find = scanner.nextInt();

        // Check if the number is present in the array
        boolean found = search3DArray(array3D, to_find);

        if (found) {
            System.out.println("The number " + to_find + " is present in the array.");
        } else {
            System.out.println("The number " + to_find + " is not present in the array.");
        }

        scanner.close();
    }

    // Method to create a 3D array
    public static int[][][] create3DArray() {
        int[][][] array3D = {
            { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} },
            { {10, 11, 12}, {13, 14, 15}, {16, 17, 18} },
            { {19, 20, 21}, {22, 23, 24}, {25, 26, 27} }
        };
        return array3D;
    }

    // Method to display a 3D array
    public static void display3DArray(int[][][] array3D) {
        for (int[][] matrix2D : array3D) {
            for (int[] row : matrix2D) {
                for (int element : row) {
                    System.out.print(element + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }

    // Method to search for a number in a 3D array
    public static boolean search3DArray(int[][][] array3D, int to_find) {
        for (int[][] matrix2D : array3D) {
            for (int[] row : matrix2D) {
                for (int element : row) {
                    if (element == to_find) {
                        return true; // Number found
                    }
                }
            }
        }
        return false; // Number not found
    }
}
