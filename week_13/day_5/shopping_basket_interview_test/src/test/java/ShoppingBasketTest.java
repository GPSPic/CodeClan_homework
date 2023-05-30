import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class ShoppingBasketTest {

    Item melon;
    Item bike;
    ShoppingBasket shoppingBasket;

    @Before
    public void before() {
        melon = new Item("Melon", 1.5);
        bike = new Item("Bike", 30);
        shoppingBasket = new ShoppingBasket();
    }

    @Test
    public void basketStartsEmpty() {
        assertEquals(0, shoppingBasket.getBasket().size());
    }

    @Test
    public void canAddToBasket() {
        shoppingBasket.addItem(melon);
        assertEquals(1, shoppingBasket.getBasket().size());
    }

    @Test
    public void canRemoveFromBasket() {
        shoppingBasket.addItem(melon);
        assertEquals(1, shoppingBasket.getBasket().size());
        shoppingBasket.removeItem(melon);
        assertEquals(0, shoppingBasket.getBasket().size());
    }

    @Test
    public void canRemoveSelectedItemFromBasket() {
        shoppingBasket.addItem(melon);
        assertEquals(1, shoppingBasket.getBasket().size());
        shoppingBasket.addItem(bike);
        shoppingBasket.removeItem(melon);
        assertEquals(1, shoppingBasket.getBasket().size());
    }

    @Test
    public void canEmptyBasket() {
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(bike);
        shoppingBasket.emptyBasket();
        assertEquals(0, shoppingBasket.getBasket().size());
    }

    @Test
    public void canCountItemsInBasket() {
        shoppingBasket.addItem(melon);
        assertEquals(1, shoppingBasket.itemCount(melon));
        assertEquals(0, shoppingBasket.itemCount(bike));
    }



//    @Test
//    public void canFindNumberOfItemsInBasket() {
//        shoppingBasket.addItem(melon);
//        shoppingBasket.addItem(melon);
//        shoppingBasket.addItem(melon);
//        shoppingBasket.addItem(bike);
//        shoppingBasket.addItem(bike);
//        assertEquals(3, shoppingBasket.itemCount(melon));
//        assertEquals(2, shoppingBasket.itemCount(bike));
//    }

//    @Test
//    public void buyOneGetOneFree() {
//        shoppingBasket.addItem(melon);
//        shoppingBasket.addItem(melon);
//        double totalValue = shoppingBasket.calculateValue();
//        assertEquals(1.5, totalValue, 0);
//    }
}
