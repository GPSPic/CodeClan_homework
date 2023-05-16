import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class LibraryTest {

    Library library;
    Library smollLibrary;
    Book book1;
    Book book2;
    Book book3;

    @Before
    public void before(){
        book1 = new Book("1964", "George Orwell", "Science-Fiction");
        book2 = new Book("It", "Stephen King", "Horror");
        book3 = new Book("Java and you", "Sid Istic", "Psychological Horror");
        library = new Library(5000);
        smollLibrary = new Library(1);
    }

    @Test
    public void testBookCounter() {
        assertEquals(0, library.getStockCount());
    }

    @Test
    public void testAddBook() {
        library.addBook(book1);
        assertEquals(1, library.getStockCount());
    }

    @Test
    public void testAddBookStockFull() {
        smollLibrary.addBook(book1);
        smollLibrary.addBook(book3);
        assertEquals(1, smollLibrary.getStockCount());
    }
}
