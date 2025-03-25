class UsernameLengthFailure(Exception):
    pass

class InvalidNameLength(Exception):
    pass

class InsufficientSalary(Exception):
    pass

def validate_person(name, salary):
    if len(name) < 3:
        raise InvalidNameLength("Name must be at least 3 characters long")
    if salary < 10000:
        raise InsufficientSalary("Salary must be at least 10000")


def validate_username(username):
    if len(username) < 4 or len(username) > 8:
        raise UsernameLengthFailure("Username must be between 4 and 8 characters long")


try:
    name = input("Enter your name: ")
    salary = float(input("Enter your salary: "))
    validate_person(name, salary)
    print("Name and salary are valid")
except InvalidNameLength as e:
    print(e)
except InsufficientSalary as e:
    print(e)

try:
    username = input("Enter your username: ")
    validate_username(username)
    print("Username is valid")
except UsernameLengthFailure as e:
    print(e)
