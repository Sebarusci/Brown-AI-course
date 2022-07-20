#Task II
number = input("Type (y) to convert hours or type (n) to convert minutes: ")
if number == "y":
    Hours = input("Number of hours: ")
    int_hours = int(Hours)
    n_minutes = int_hours * 60
    print(str(int_hours) + " hours Is " + str(n_minutes) + " minutes.")
elif number == "n":
    Minutes = input("Number of minutes: ")
    int_minutes = int(Minutes)
    n_hours = int_minutes / 60
    print(str(int_minutes) + " minutes Is " + str(n_hours) + " hours.")
else:
    print("Plase run the rogramm again and select one of the options.")