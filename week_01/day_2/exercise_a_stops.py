stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
stops.append("Edinburgh Waverley")
stops.insert(0, "Glasgow Queen Street")
stops.insert(4, "Polmont")
print(stops.index("Linlithgow"))
stops.pop(stops.index("Livingston"))
stops.pop(2)
# First attempt at a dirty solution, but that does not survive simple things like adding stops or modifying the list.
# stops_number = stops.index("Edinburgh Waverley") + 1
# print(stops_number)
# Some Googling later, remembered a more solid way with len
print(len(stops))
stops.sort()
stops.reverse()

for stop in stops:
    print(stop)

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop