class Shape {
    private String color;
    private boolean filled;

    public Shape() {
        this.color = "green";
        this.filled = true;
    }

    public Shape(String color, boolean filled) {
        this.color = color;
        this.filled = filled;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public boolean isFilled() {
        return filled;
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    @Override
    public String toString() {
        return "A Shape with color of " + color + " and " + (filled ? "filled" : "Not filled");
    }
}

class Circle extends Shape {
    private double radius;

    public Circle() {
        this.radius = 1.0;
    }

    public Circle(double radius) {
        this.radius = radius;
    }

    public Circle(double radius, String color, boolean filled) {
        super(color, filled);
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double getArea() {
        return Math.PI * radius * radius;
    }

    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width;
    private double length;

    public Rectangle() {
        this.width = 1.0;
        this.length = 1.0;
    }

    public Rectangle(double width, double length) {
        this.width = width;
        this.length = length;
    }

    public Rectangle(double width, double length, String color, boolean filled) {
        super(color, filled);
        this.width = width;
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getArea() {
        return width * length;
    }

    public double getPerimeter() {
        return 2 * (width + length);
    }
}

class Cylinder extends Circle {
    private double height;

    public Cylinder() {
        super();
        this.height = 1.0;
    }

    public Cylinder(double radius, double height) {
        super(radius);
        this.height = height;
    }

    public Cylinder(double radius, double height, String color, boolean filled) {
        super(radius, color, filled);
        this.height = height;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    @Override
    public double getArea() {
        return 2 * Math.PI * getRadius() * height + 2 * super.getArea();
    }
}

public class Shapes {
    public static void main(String[] args) {
        Shape shape1 = new Shape();
        System.out.println(shape1);

        Circle circle1 = new Circle(2.0, "blue", false);
        System.out.println(circle1);
        System.out.println("Area of circle: " + circle1.getArea());
        System.out.println("Perimeter of circle: " + circle1.getPerimeter());

        Rectangle rectangle1 = new Rectangle(2.0, 3.0, "red", true);
        System.out.println(rectangle1);
        System.out.println("Area of rectangle: " + rectangle1.getArea());
        System.out.println("Perimeter of rectangle: " + rectangle1.getPerimeter());

        Cylinder cylinder1 = new Cylinder(2.0, 3.0, "green", true);
        System.out.println(cylinder1);
        System.out.println("Area of cylinder: " + cylinder1.getArea());
    }
}

