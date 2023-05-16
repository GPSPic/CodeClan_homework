import java.util.ArrayList;

public class Library {

    private ArrayList<Book> stock;
    private int capacity;

    public Library(int capacity){
        this.stock = new ArrayList<>();
        this.capacity = capacity;
    }

    public int getStockCount() {
        return this.stock.size();
    }

    public void addBook(Book book) {
        if (getStockCount() < this.capacity) {
            this.stock.add(book);
        }
    }
}
