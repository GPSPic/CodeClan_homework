import java.sql.Array;
import java.util.*;

public class ShoppingBasket {

    private HashMap<Item, Integer> basket;
    private double itemsValue;

    public ShoppingBasket() {
        this.basket = new HashMap<>();
        this.itemsValue = 0;
    }

    public double getItemsValue() {
        return this.itemsValue;
    }

    public HashMap<Item, Integer> getBasket() {
        return this.basket;
    }

    public void addItem(Item item) {
        if (this.basket.containsKey(item)) {
            this.basket.put(item, (this.basket.get(item) + 1));
        } else {
            this.basket.put(item, 1);
        }
    }

    public void removeItem(Item item) {
        this.basket.remove(item);
    }

    public void emptyBasket() {
        this.basket.clear();
    }

    public int itemCount(Item item) {
        return this.basket.getOrDefault(item, 0);
    }

}
