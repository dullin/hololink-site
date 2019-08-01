import javax.swing.*;
import java.awt.*;
import java.awt.geom.RoundRectangle2D;
import java.util.ArrayList;

public class HanoiTowerComponent extends JComponent {

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;

        RoundRectangle2D bottom = new RoundRectangle2D.Double( 20, 270, 150, 20.0, 10.0, 10.0);
        RoundRectangle2D pillar = new RoundRectangle2D.Double(90, 30, 20, 250, 10, 10);
        g2.fill(bottom);
        g2.fill(pillar);
        Dimension d = new Dimension(200,350);
        setSize(d);
        setMinimumSize(d);
        setMaximumSize(d);
    }


    public static void main(String[] args) {
        JFrame frame = new JFrame();

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        Dimension d = new Dimension(200,350);
        frame.setSize(d);
        frame.setMinimumSize(d);
        frame.setMaximumSize(d);

        frame.add(new HanoiTowerComponent());

        frame.setVisible(true);

    }
}
