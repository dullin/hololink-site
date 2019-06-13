package org.hololink.life;

import org.junit.jupiter.api.Test;

import static org.hololink.life.CellState.*;
import static org.junit.jupiter.api.Assertions.*;

class NeighborhoodTest {

    @Test
    void liveCount() {
        CellState[][]  testGrid = new CellState[4][4];

        testGrid[0][0] = ALIVE;
        testGrid[0][1] = DEAD;
        testGrid[0][2] = DEAD;
        testGrid[0][3] = DEAD;

        testGrid[1][0] = DEAD;
        testGrid[1][1] = ALIVE;
        testGrid[1][2] = DEAD;
        testGrid[1][3] = DEAD;

        testGrid[2][0] = DEAD;
        testGrid[2][1] = ALIVE;
        testGrid[2][2] = DEAD;
        testGrid[2][3] = ALIVE;

        testGrid[3][0] = ALIVE;
        testGrid[3][1] = ALIVE;
        testGrid[3][2] = DEAD;
        testGrid[3][3] = DEAD;

        Neighborhood n = new Neighborhood(testGrid, 1, 1);
        Neighborhood n2 = new Neighborhood(testGrid, 0, 0);

        assertEquals(3, n.liveCount());
        assertEquals(4, n2.liveCount());
    }
}