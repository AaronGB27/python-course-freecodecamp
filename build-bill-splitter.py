running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print(f"Total bill so far {round(running_total, 2)}")

tip = running_total * 0.25
print(f"Tip amount: {round(tip, 2)}")

final_bill = running_total / num_of_friends
print(f"Bill per person: {round(final_bill, 2)}")
