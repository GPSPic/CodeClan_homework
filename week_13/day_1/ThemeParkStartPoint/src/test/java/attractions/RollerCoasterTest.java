package attractions;

import org.junit.Before;
import org.junit.Test;
import people.Visitor;

import static org.junit.Assert.*;

public class RollerCoasterTest {

    Visitor visitor1;
    Visitor visitor2;
    Visitor visitor3;
    Visitor visitor4;
    RollerCoaster rollerCoaster;

    @Before
    public void setUp() {
        visitor1 = new Visitor(11, 175, 10);
        visitor2 = new Visitor(111, 145, 10);
        visitor3 = new Visitor(111, 175, 10);
        visitor4 = new Visitor(111, 275, 20);
        rollerCoaster = new RollerCoaster("Blue Ridge", 10);
    }

    @Test
    public void hasName() {
        assertEquals("Blue Ridge", rollerCoaster.getName());
    }

    @Test
    public void hasRating() {
        assertEquals(10, rollerCoaster.getRating());
    }

    @Test
    public void hasVisitCount() {
        assertEquals(0, rollerCoaster.getVisitCount());
    }

    @Test
    public void testIsAllowedTo() {
        assertFalse(rollerCoaster.isAllowedTo(visitor1));
        assertFalse(rollerCoaster.isAllowedTo(visitor2));
        assertTrue(rollerCoaster.isAllowedTo(visitor3));
    }

    @Test
    public void testPriceFor() {
        assertEquals(8.4, rollerCoaster.priceFor(visitor3), 0);
        assertEquals(16.8, rollerCoaster.priceFor(visitor4), 0);
    }
}
