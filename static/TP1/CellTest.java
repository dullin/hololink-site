package org.hololink.life;

import org.junit.Test;
import static org.junit.Assert.*;

import static org.hololink.life.CellState.*;

public class CellTest {

    @Test
    public void getState() {
        Cell c1 = new Cell();
        Cell c2 = new Cell(ALIVE);

        assertEquals(c1.getState(), DEAD);
        assertEquals(c2.getState(), ALIVE);
    }

    @Test
    public void getNextState() {
        Cell c1 = new Cell(DEAD);

        assertEquals(ALIVE, c1.getNextState(3));

        c1.setState(ALIVE);
        assertEquals(DEAD, c1.getNextState(2));
        assertEquals(ALIVE, c1.getNextState(4));
    }

    @Test
    public void setState() {
        Cell c = new Cell();

        c.setState(ALIVE);
        assertEquals(c.getState(), ALIVE);
        c.setState(DEAD);
        assertEquals(c.getState(), DEAD);

    }
}