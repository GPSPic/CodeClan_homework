import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ItemTest {

    Item melon;

    @Before
    public void before() {
        melon = new Item("Melon", 1.5);
    }

    @Test
    public void hasName() {
        assertEquals("Melon", melon.getName());
    }

    @Test
    public void hasPrice() {
        assertEquals(1.5, melon.getPrice(), 0);
    }
}
