from datetime import date


name = input("Enter your firstname: ")
last = input("Enter your lastname: ")
birth_year = int(input("Enter your year of birth: "))

# print(name[0])


def getInfo(nameUser, lastUser, bDayUser):
    today_year = int(date.today().year)
    age = today_year - bDayUser
    return "Your initials are {}{} and you are {} years old".format(nameUser[0], lastUser[0], age)


print(getInfo(name, last, birth_year))
