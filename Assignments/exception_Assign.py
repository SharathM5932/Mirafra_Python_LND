# 1. Write a program to raise exception
# a. enter name of the person raise exception where it is below 3 letters
# b. enter salary of the person raise exception when salary below 10000

class InvalidNameException(Exception):
    pass
class InvalidSalaryException(Exception):
    pass
def validate_person(name,salary):
    if len(name)<3:
        raise InvalidNameException("Name must have at least 3 letters.")
    if salary<10000:
        raise InvalidSalaryException("Salary must be at least 10000")
def main():
    try:
        name=input('Enter the person name:')
        salary=float(input('Enter the Salary'))
        validate_person(name,salary)
        print('Validation successful')
    except InvalidNameException as n:
        print(f'Error:{n}')
    except InvalidSalaryException as n:
        print(f'Error:{n}')
    except ValueError:
        print("Error: Salary must be a numeric value.")
main()

