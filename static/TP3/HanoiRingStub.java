import javax.swing.*;
import java.awt.*;
import java.awt.geom.Rectangle2D;

import static java.awt.Color.*;

public class HanoiRingStub extends JComponent {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;

        int width = 3 * 20 + 20;

        Rectangle2D ring = new Rectangle2D.Double(getWidth()/2 - width/2, getHeight()/2 - 15/2, width, 15);

        g2.setColor(GRAY);

        g2.fill(ring);

    }

    public static void main(String[] args) {
        JFrame frame = new JFrame();

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setSize(100,50);

        frame.add(new HanoiRingStub());

        frame.setVisible(true);
    }

}
