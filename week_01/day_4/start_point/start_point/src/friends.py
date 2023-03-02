def get_name(person):
    name = person["name"]
    return name

def get_favourite_tv_show(tv_show):
    favourite_show = tv_show["favourites"]["tv_show"]
    return favourite_show

def likes_to_eat(person, food):
    snack_food = False
    if person["favourites"]["snacks"].count(food) > 0:
        snack_food = True
    return snack_food

def add_friend(person, new_friend):
    friend = person["friends"]
    friend.append(new_friend)

def remove_friend(person, former_friend):
    friend = person["friends"]
    index_former_friend = friend.index(former_friend)
    friend.pop(index_former_friend)

def lend_money(person_1, person_2, money):
    person_1["monies"] -= money
    person_2["monies"] += money

def total_money(people):
    total = 0
    for person in people:
            total += person["monies"]
    return total

def all_favourite_foods(people):
    fav_foods = []
    for person in people:
        fav_foods += person["favourites"]["snacks"]
        # fav_foods.append(person["favourites"]["snacks"])
        # person["favourites"]["snacks"].pop(0)
    return fav_foods

def find_no_friends(people):
    all_alone = []
    for person in people:
        if len(person["friends"]) == 0:
            all_alone.append(person)
    return all_alone

def unique_favourite_tv_shows(people):
    unique_tv_shows = []

    for person in people:
        shared_tv_love = unique_tv_shows.count(person["favourites"]["tv_show"])

        if shared_tv_love == 0:
            unique_tv_shows.append(person["favourites"]["tv_show"])
    return unique_tv_shows

# def unique_favourite_tv_shows_set(people):
#     unique_tv_shows_list = unique_favourite_tv_shows
#     print(unique_tv_shows_list(people))
#     tv_shows_set = set(unique_tv_shows_list(people))
#     print(tv_shows_set(people))
#     return tv_shows_set

def unique_favourite_tv_shows_set(people):
    unique_tv_shows = set()
    for person in people:
            unique_tv_shows.add(person["favourites"]["tv_show"])
    return unique_tv_shows