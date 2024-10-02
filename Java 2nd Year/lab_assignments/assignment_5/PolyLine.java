import java.util.ArrayList;

public class PolyLine {
    public static void main(String[] args) {
        PolyLine main = new PolyLine(); // Create an instance of Main class
        main.execute(); // Call the execute method
    }

    public void execute() { // Instance method to avoid static context
        Polyline polyline = new Polyline();
        polyline.addPoint(new Point(0, 0));
        polyline.addPoint(new Point(1, 1));
        polyline.addPoint(new Point(2, 2));

        System.out.println("Points in polyline: " + polyline);
        polyline.getLength();
    }

    static class Point {
        private int x;
        private int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return this.x;
        }

        public void setX(int new_x) {
            this.x = new_x;
        }

        public int getY() {
            return this.y;
        }

        public void setY(int new_y) {
            this.y = new_y;
        }
    }

    static class Polyline {
        private ArrayList<Point> points;

        public Polyline() {
            this.points = new ArrayList<>();
        }

        public void addPoint(Point point) {
            points.add(point);
        }

        public String toString() {
            StringBuilder string = new StringBuilder();
            for (int i = 0; i < points.size(); i++) {
                string.append("(").append(points.get(i).getX()).append(",").append(points.get(i).getY()).append(")");
            }
            return string.toString();
        }

        public void getLength() {
            float total_length = 0;
            for (int i = 0; i < points.size() - 1; i++) {
                Point p1 = points.get(i);
                Point p2 = points.get(i + 1);
                total_length += Math.sqrt(Math.pow(p2.getX() - p1.getX(), 2) + Math.pow(p2.getY() - p1.getY(), 2));
            }
            System.out.println("Length of the polyline: " + total_length);
        }
    }
}


