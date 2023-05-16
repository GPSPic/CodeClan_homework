import java.util.HashMap;

public class Runner {

    public static void main(String[] args) {
        HashMap<String, String> favouriteFruits = new HashMap<>();

        favouriteFruits.put("Alice", "Apple");
        favouriteFruits.put("Beatrice", "Baobab");
        favouriteFruits.put("Carole", "Carrot");

        System.out.println(favouriteFruits.get("Alice"));

        favouriteFruits.put(key, value) // inserts a new entry into the HashMap
        favouriteFruits.get(key) // gets the value for the given key
        favouriteFruits.size() // returns the size of the HashMap as an integer
        favouriteFruits.clear() // clears all entries from the HashMap
        favouriteFruits.containsValue(value) // returns true if the HashMap contains the value
        favouriteFruits.remove(key) //removes the entry with the given key
    }
}
