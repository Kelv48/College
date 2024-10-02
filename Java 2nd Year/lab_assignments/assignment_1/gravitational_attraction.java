// A2
// Kelvin Osagie 122318693

public class gravitational_attraction {
    public static void main(String[] args) {
       float Earth_weight = 50.0f;
       String[] planets = {"Earth", "Mercury", "Venus", "Jupiter", "Saturn"};
       float[] multipliers = {1.0f, 0.4f, 0.9f, 2.5f, 1.1f};
       System.out.printf("%-15s%-15s%-15s%n", "Planet", "Multiplier", "Alice Weight");

       for (int i = 0; i < planets.length; i++) {
        float result = Earth_weight * multipliers[i];

        System.out.printf("%-15s%-15.1f%-15.1fKg%n", planets[i], multipliers[i], result);
       }
       
    }
}
