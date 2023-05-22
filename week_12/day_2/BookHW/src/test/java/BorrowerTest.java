import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BorrowerTest {

    Borrower borrower;
    Library library;
    Book book1;
    Book book2;
    Book book3;

    @Before
    public void before() {
        book1 = new Book("1964", "George Orwell", "Science-Fiction");
        book2 = new Book("It", "Stephen King", "Horror");
        book3 = new Book("Java and you", "Sid Istic", "Psychological Horror");
        library = new Library(5000);
        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        borrower = new Borrower();
    }

    @Test
    public void testBorrowedCounter() {
        assertEquals(0, borrower.getBorrowedBooksCount());
    }

//    @Test
//    public void testBorrowBook() {
//        borrower.borrowBook(library);
//        assertEquals(1, borrower.getBorrowedBooksCount());
//    }
}

