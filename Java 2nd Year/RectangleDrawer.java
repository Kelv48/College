import javax.swing.*;
import java.awt.*;

public class RectangleDrawer extends JPanel {
    
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        
        // Draw a filled rectangle
        g2d.setColor(Color.BLUE);
        g2d.fillRect(50, 50, 100, 50); // x, y, width, height
        
        // Draw an outlined rectangle
        g2d.setColor(Color.RED);
        g2d.drawRect(200, 50, 100, 50); // x, y, width, height
    }
    
    public static void main(String[] args) {
        JFrame frame = new JFrame("Rectangle Drawer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLocationRelativeTo(null);
        
        RectangleDrawer drawer = new RectangleDrawer();
        frame.add(drawer);
        
        frame.setVisible(true);
    }
}