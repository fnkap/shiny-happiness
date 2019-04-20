"""The Revised Julian Calendar

Background
The Revised Julian Calendar is a calendar system very similar to the familiar Gregorian Calendar, but slightly more
accurate in terms of average year length. The Revised Julian Calendar has a leap day on Feb 29th of leap years as
follows:

Years that are evenly divisible by 4 are leap years.

Exception: Years that are evenly divisible by 100 are not leap years.

Exception to the exception: Years for which the remainder when divided by 900 is either 200 or 600 are leap years.

For instance, 2000 is an exception to the exception: the remainder when dividing 2000 by 900 is 200. So 2000 is a leap
year in the Revised Julian Calendar.


Challenge
Given two positive year numbers (with the second one greater than or equal to the first), find out how many leap days
(Feb 29ths) appear between Jan 1 of the first year, and Jan 1 of the second year in the Revised Julian Calendar.
This is equivalent to asking how many leap years there are in the interval between the two years,
including the first but excluding the second."""


def leap_count(year):
    leaps_base = (year // 900) * 218  # In a batch of 900 years there are 218 leap years

    # Do a for cycle to calculate leap years the remaining years
    years_to_calc = year % 900

    for i in range(years_to_calc):
        if i % 4 == 0:
            leaps_base += 1
        if i % 100 == 0:
            leaps_base -= 1
        if (i % 900 == 200) or (i % 900 == 600):
            leaps_base += 1

    return leaps_base


def leaps(year1, year2):
    if not year2 > year1:
        print(f"{year2} is not greater than {year1}.")
        exit()
    value = leap_count(year2) - leap_count(year1)
    print(value)


leaps(123456789101112, 1314151617181920)
