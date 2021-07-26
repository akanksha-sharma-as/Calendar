## For Calculating Starting Day Of A Month
## m represents Month 
## year_starting Represents From Which Day Does Year Starts

def non_leap_month(m, year_starting):
    switcher={
        1:  year_starting,
        2: ( year_starting+3)%7,
        3: ( year_starting+3)%7,
        4: ( year_starting+6)%7,
        5: ( year_starting+8)%7,
        6: ( year_starting+11)%7,
        7: ( year_starting+13)%7,
        8: ( year_starting+16)%7,
        9: ( year_starting+19)%7,
        10: year_starting,             #( year_starting+14)%7 =  year_starting
        11: ( year_starting+24)%7,
        12: ( year_starting+26)%7
    }
    return (switcher.get(m,"Invalid Month"))

def leap_month(m, year_starting):
    switcher={
        1:  year_starting,
        2: ( year_starting+3)%7,
        3: ( year_starting+4)%7,
        4: year_starting,              #( year_starting+7)%7 =  year_starting
        5: ( year_starting+9)%7,
        6: ( year_starting+12)%7,
        7: year_starting,              #( year_starting+14)%7 =  year_starting
        8: ( year_starting+17)%7,
        9: ( year_starting+20)%7,
        10: ( year_starting+22)%7,
        11: ( year_starting+25)%7,
        12: ( year_starting+27)%7
    }
    return (switcher.get(m,"Invalid Month"))
