import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BookTest {

    Book book1;
    Book book2;
    Book book3;

    @Before
    public void before() {
        book1 = new Book("1964", "George Orwell", "Science-Fiction");
        book2 = new Book("It", "Stephen King", "Horror");
        book3 = new Book("Java and you", "Sid Istic", "Psychological Horror");
    }

    @Test
    public void testHasTitle() {
        assertEquals("1964", book1.getTitle());
    }
}
