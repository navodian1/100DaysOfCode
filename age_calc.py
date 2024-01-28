# Calculate the complete age of a person in years, months and days

import datetime


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def main():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    year, month, day = map(int, dob.split('-'))
    age = calculate_age(datetime.date(year, month, day))
    print("Your age is: {}".format(age))


if __name__ == '__main__':
    main()