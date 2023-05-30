public class Customer {

    private String name;
    private boolean hasLoyaltyCard;
    private ShoppingBasket shoppingBasket;

    public Customer(String name, boolean hasLoyaltyCard) {
        this.name = name;
        this.hasLoyaltyCard = hasLoyaltyCard;
        this.shoppingBasket = new ShoppingBasket();
    }

    public String getName() {
        return this.name;
    }

    public boolean isHasLoyaltyCard() {
        return this.hasLoyaltyCard;
    }

    public ShoppingBasket getShoppingBasket() {
        return this.shoppingBasket;
    }

    public void addBasket(ShoppingBasket shoppingBasket) {
        this.shoppingBasket = shoppingBasket;
    }

    public double calculateBasketValue() {
        double totalValue = 0;
        for (Item item : this.shoppingBasket.getBasket().keySet()) {
            int itemCount = this.shoppingBasket.itemCount(item);
            int roundedUpCount =  itemCount / 2 + (itemCount % 2 == 0 ? 0 : 1);
            totalValue += item.getPrice() * roundedUpCount;
        }
        if (totalValue > 20) {
            totalValue -= totalValue * 0.1;
        }
        if (this.isHasLoyaltyCard()) {
            totalValue -= totalValue * 0.02;
        }
        return totalValue;
    }


}
