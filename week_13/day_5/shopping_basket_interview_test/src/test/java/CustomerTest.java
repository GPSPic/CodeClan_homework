import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CustomerTest {

    Item melon;
    Item bike;
    ShoppingBasket shoppingBasket;
    Customer bob;
    Customer tim;

    @Before
    public void before() {
        melon = new Item("Melon", 1.5);
        bike = new Item("Bike", 30);
        shoppingBasket = new ShoppingBasket();
        bob = new Customer("Bob", true);
        tim = new Customer("Tim", false);
    }

    @Test
    public void bobHasLoyaltyCard() {
        assertTrue(bob.isHasLoyaltyCard());
    }

    @Test
    public void timNoLoyaltyCard() {
        assertFalse(tim.isHasLoyaltyCard());
    }

    @Test
    public void canCalculateBasketContentValue() {
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(melon);
        tim.addBasket(shoppingBasket);
        double result = tim.calculateBasketValue();
        assertEquals(3, result, 0);
    }

    @Test
    public void canApply10PercentDiscount () {
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(bike);
        tim.addBasket(shoppingBasket);
        double result = tim.calculateBasketValue();
        assertEquals(29.7, result, 0);
    }

    @Test
    public void canApplyLoyaltyDiscount() {
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(melon);
        shoppingBasket.addItem(melon);
        bob.addBasket(shoppingBasket);
        double result = bob.calculateBasketValue();
        assertEquals(2.94, result, 0);
    }

    @Test
    public void canApplyAllDiscounts() {
        shoppingBasket.addItem(bike);
        shoppingBasket.addItem(bike);
        bob.addBasket(shoppingBasket);
        double result = bob.calculateBasketValue();
        assertEquals(26.46, result, 0);
    }
}
