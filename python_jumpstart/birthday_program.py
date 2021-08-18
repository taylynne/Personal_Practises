import time
import datetime


def print_header():
    print("-------------------------")
    print("   BIRTHDAY COUNTDOWN")
    print("-------------------------")
    print()


def get_birthday_from_user():
    print("When were you born?")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_between_dates():
    pass


def print_bday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    num_of_days = compute_between_dates(bday, now)
    print_bday_information(num_of_days)

