# (1) Scoop class -- each instance is one scoop of ice cream
#
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('coffee')
#
# print(s1.flavor)  # chocolate
#
# for one_scoop in [s1, s2, s3]:
#     print(one_scoop.flavor)  # chocolate, vanilla, coffee
#
# (2) Person class -- name, e-mail address, and phone number
#
#     Create several people, and iterate over them in a list
#     and print their names (similar to a phone book)
#
#     Change the e-mail address of one person, and show
#     that it has changed by printing your list a second time
#
# (3) Create a BankAccount class. It'll have a single
#     attribute (per instance), transactions -- a list of floats
#
#     Every time you deposit, append a positive float
#     Every time you withdraw, append a negative float
#
#     (a) create two different accounts
#     (b) add a number of transactions +/- to each account
#     (c) show, for each account, the number of transactions
#     and the average amount per transaction, as well as
#     the current balance.  (assume it starts at 0)
#
#
#   27 December 2020 - TB/SpaceOres
#


# EXERCISE ONE - SCOOP CLASS

class Scoop():
    # defining scoop class
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoop("chocolate")
s2 = Scoop("Vanilla")
s3 = Scoop("coffee")

print(s1.flavor)

for one_scoop in [s1, s2, s3]:
    print(one_scoop.flavor)

# EXERCISE TWO - PERSON CLASS

class person():
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

person_one = person("Bruce", "bShort1@gmail.com", "5805830912")
person_two = person("Clover", "cloDev@hotmail.com", "9996660934")
person_three = person("Buddy", "mountainLyon@gmail.com", "8595592483")
person_four = person("Lily", "bananasrul3@live.com", "3606549383")

people = [person_one, person_two, person_three, person_four]

for information in people:
    print(f"{information.name}'s email and phone number is: {information.email}, {information.phone_number}")

person_one.email = "bruceBanner@gmail.com"

for information in people:
    print(f"{information.name}'s email and phone number is: {information.email}, {information.phone_number}")


# EXERCISE THREE - BANKACCOUNT CLASS


