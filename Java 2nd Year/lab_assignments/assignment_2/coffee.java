import java.util.Scanner;

public class coffee {
    public static void main(String args[]) {
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Please enter the weight of coffee in pounds ");
    double weightPer = scan.nextFloat();

    System.out.println("Please enter number of bags sold ");
    int numSold = scan.nextInt();

    double pricePerPound = 5.99;
    double salesTax = 0.0725;   

    double totalPrice = weightPer * numSold * pricePerPound;
    double totalPriceWithTax = totalPrice * salesTax;

    System.out.println("Number of bags sold: " + numSold);
    System.out.println("Weight per bag: " + weightPer + " lb");
    System.out.println("Price per pound: $" + pricePerPound);
    System.out.println("Sales tax: 7.25%");
    System.out.printf("Total price: $ %.3f%n", totalPriceWithTax);

    scan.close();
    }
}
