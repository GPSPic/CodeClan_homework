day_of_week = "Monday"
current_week = 1
current_day_of_week = 1

print("Today is " + day_of_week + ", day " + str(current_day_of_week) + " of week " + str(current_week) + " of studying at Codeclan.")

current_week = 1
current_day_of_week = 1
total_week_of_course = 16
total_course_day_per_week = 5

def weeks_to_go():
    weeks_left = total_week_of_course - current_week
    days_left = total_course_day_per_week - current_day_of_week
    print("Only " + str(days_left) + " days and " + str(weeks_left) + " weeks left in the course!")

def motivate_me():
    print("DON'T PANIC!")
#I can't believe we almost passed on a H2G2 reference

weeks_to_go()
motivate_me()
