from application.salary import calculate_salary as sal
from application.db.people import get_employees as peo
import datetime


if __name__ == "__main__":
    print(datetime.datetime.now())
    a = sal()
    print(a)
    peo()
