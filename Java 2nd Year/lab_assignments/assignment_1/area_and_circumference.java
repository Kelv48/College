// A2

public class area_and_circumference {
    public static void main(String[] args) {
        float PI = 3.14f;
        float radius = 181.55f;
        //circle area = pi*r*r
        //circumference = 2*pi*r
        float area = PI * (radius*radius);
        float circumference = 2 * PI * radius;
        System.out.println("The area of the circle is " + area + " square units");
        System.out.println("The circumference of the circle is " + circumference +" units");
    }
}
