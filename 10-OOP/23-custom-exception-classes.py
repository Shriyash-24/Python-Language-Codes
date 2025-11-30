# Custom exceptions - User defined exceptions.
# Why are we learning custom exceptions? - We needed to know the concepts of classes.
# Exception are classes actually.
# The class hierarchy for built in exceptions is..
# BaseException is parent of all exception. We usually use Exception.

class SalaryError(Exception):
    pass

def get_salary(salary):
    if salary < 0:
        raise SalaryError("Salary Can't be negative")
    else:
        bonus = 0.1 * salary
        return salary + bonus

salary = int(input("Enter Salary: "))
final_salary = get_salary(salary)
print(final_salary)


