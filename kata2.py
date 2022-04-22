from operator import truediv

def isLeapYear(nb):
    return nb%400 == 0 or nb %4 == 0 and nb%100 != 0


print("1700 should not be a leap year => ", isLeapYear(1700))
print("1800 should not be a leap year => ", isLeapYear(1800))
print("2020 should not be a leap year => ", isLeapYear(2020))
print("2000 should not be a leap year => ", isLeapYear(2000))
print("1700 should not be a leap year => ", isLeapYear(1700))
print("1700 should not be a leap year => ", isLeapYear(1700))
print("1700 should not be a leap year => ", isLeapYear(1700))
