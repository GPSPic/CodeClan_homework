from models.order import Order
import datetime

order1 = Order("Kevin", datetime.date(2023, 3, 15), 4500, "Licorice")
order2 = Order("Karen", "14 March 2023", 2, "Tutti Fruti")
orders = [order1, order2]