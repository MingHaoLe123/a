week = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}


day = input("Enter a day of the week: ").strip().capitalize()


if day in week:
  number = week[day]
  print(f" {day} is day {number}")
else:
    print("Please enter a valid day")