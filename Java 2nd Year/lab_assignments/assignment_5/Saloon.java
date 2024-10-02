class Customer {
    private String name;
    private String membership;

    public Customer(String name, String membership) {
        this.name = name;
        this.membership = membership;
    }

    public String getMembership() {
        return membership;
    }

    public void setMembership(String membership) {
        this.membership = membership;
    }

    @Override
    public String toString() {
        return "Customer: " + name + ", Membership: " + membership;
    }
}

class Discount {
    public static final double PREMIUM_DISCOUNT = 0.20;
    public static final double GOLD_DISCOUNT = 0.15;
    public static final double SILVER_DISCOUNT = 0.10;
    public static final double PRODUCT_DISCOUNT = 0.10;

    public static double applyServiceDiscount(double totalServiceCost, String membership) {
        if (membership != null) {
            switch (membership) {
                case "Premium":
                    return totalServiceCost * (1 - PREMIUM_DISCOUNT);
                case "Gold":
                    return totalServiceCost * (1 - GOLD_DISCOUNT);
                case "Silver":
                    return totalServiceCost * (1 - SILVER_DISCOUNT);
                default:
                    return totalServiceCost;
            }
        } else {
            // No membership, return original cost
            return totalServiceCost;
        }
    }

    public static double applyProductDiscount(double totalProductCost) {
        return totalProductCost * (1 - PRODUCT_DISCOUNT);
    }
}

class Visit {
    private Customer customer;
    private double serviceCost;
    private double productCost;

    public Visit(Customer customer, double serviceCost, double productCost) {
        this.customer = customer;
        this.serviceCost = serviceCost;
        this.productCost = productCost;
    }

    public double totalBill() {
        double totalServiceCost = Discount.applyServiceDiscount(serviceCost, customer.getMembership());
        double totalProductCost = Discount.applyProductDiscount(productCost);
        return totalServiceCost + totalProductCost;
    }
}

public class Saloon {
    public static void main(String[] args) {
        // Create customers
        Customer customer1 = new Customer("Alice", "Premium");
        Customer customer2 = new Customer("Bob", "Gold");
        Customer customer3 = new Customer("Charlie", "Silver");
        Customer customer4 = new Customer("David", null);

        // Create visits
        Visit visit1 = new Visit(customer1, 100, 50);
        Visit visit2 = new Visit(customer2, 100, 50);
        Visit visit3 = new Visit(customer3, 100, 50);
        Visit visit4 = new Visit(customer4, 100, 50);

        // Display bills
        System.out.println("Visit 1 Total Bill: " + visit1.totalBill());
        System.out.println("Visit 2 Total Bill: " + visit2.totalBill());
        System.out.println("Visit 3 Total Bill: " + visit3.totalBill());
        System.out.println("Visit 4 Total Bill: " + visit4.totalBill());
    }
}
