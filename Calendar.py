import sys
sys.path.append("C:\\Users\\my\\google drive\\Calender")
from Leap_year import leap_year
from Month import leap_month,non_leap_month
from Printing import leap_printing,non_leap_printing
from Year_starting import year_starting

year=int(input("Enter year(yyyy) : "))
m=int(input("Enter Month(1-12) : "))

M=[" ","January","February","March","April","May","June","July","August","September","October","November","December"]

Year_starting=year_starting(year)               # for calculating from which day the given year starts
if leap_year(year)==True:                       # for calculating given year is leap year or not
    print(M[m]," ",year)
    p=(leap_month(m,Year_starting))             # for calculating from which day month starts for given leap year
    if p==0:                                    # 0 is returned when 7%7 expression works bt we want 7 so, we change it here (Month module)
        p=7
    leap_printing(p,m)                          # for printing calendar of leap year
else:
    print(M[m]," ",year)
    p=(non_leap_month(m,Year_starting))         # for calculating from which day month starts for given non-leap year
    if p==0:                                    # 0 is returned when 7%7 expression works bt we want 7 so, we change it here (Month module)
        p=7
    non_leap_printing(p,m)                      # for printing calendar of non-leap year