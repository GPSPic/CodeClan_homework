import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrinterTest {

    Printer printer;

    @Before
    public void before() {
        printer = new Printer(500, 100);
    }

    @Test
    public void hasPaper() {
        assertEquals(500, printer.getRemainingPaper());
    }

    @Test
    public void hasToner() {
        assertEquals(100, printer.getTonerLevel());
    }

    @Test
    public void canPrint() {
        printer.print(10, 10);
        assertEquals(400, printer.getRemainingPaper());
    }

    @Test
    public void cannotPrint() {
        printer.print(100, 6);
        assertEquals(500, printer.getRemainingPaper());
    }

    @Test
    public void decreaseTonerLevel() {
        printer.print(10, 8);
        assertEquals(20, printer.getTonerLevel());
    }

    @Test
    public void printBlankPages() {
        printer.print(10, 12);
        assertEquals(0, printer.getTonerLevel());
    }
}
