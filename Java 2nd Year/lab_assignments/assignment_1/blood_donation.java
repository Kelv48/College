// A2

public class blood_donation {
    public static void main(String[] args) {
        checkBlood("Alice", 50, 19);
        checkBlood("Bob", 36, 20);
        checkBlood("Jemmy", 45, 17);
        checkBlood("Clive", 100, 80);
    }

    private static void checkBlood(String name, int weight, int age) {
        if (age >= 18 && age <= 60 && weight > 40) {
            System.out.println(name + " can donate blood.");
        } else {
            System.out.println(name + " cannot donate blood.");
            if (age < 18) {
                System.out.println("Reason: Age is below 18.");
            } else if (age > 60) {
                System.out.println("Reason: Age is above 60.");
            } else if (weight <= 40) {
                System.out.println("Reason: Weight is 40kg or below");
            }
        }
        System.out.println("\n");
    }
}
