## For Calculating From Which Day The Year Starts

def year_starting(year):
    y=year//100                 ## for knowing starting 2 digits of year (century year)
    if year==1900:               ## 1900 does not match with 1901-1999 logic
        return 2
    elif year==1800:            ## 1800 does not match with 1801-1899 logic
        return 4
    elif y==19 or y==20 or y==18:
        yy=year-(y)*100             ## for knowing last 2 digits of year 
        n=yy%28                     ## after every 28 days the days repeat (7*4=28) (7 for weekdays)(4 coz after every 4 year there is a leap year)
        if (n==00 or n==5 or n==11 or n==22):       ## for each have same days
            if y==18:                               ## for 18 century
                return 3
            elif y==19:                             ## for 19 century
                return 1
            else:                                   ## for 20 century
                return 7
        elif (n==6 or n==12 or n==17 or n==23):     ## for each have same days
            if y==18:                               ## for 18 century
                return 4
            elif y==19:                             ## for 19 century
                return 2
            else:                                   ## for 20 century
                return 1
        elif (n==1 or n==7 or n==18 or n==24):      ## for each have same days
            if y==18:                               ## for 18 century
                return 5
            elif y==19:                             ## for 19 century
                return 3
            else:                                   ## for 20 century
                return 2
        elif (n==2 or n==8 or n==13 or n==19):      ## for each have same days
            if y==18:                               ## for 18 century
                return 6
            elif y==19:                             ## for 19 century
                return 4
            else:                                   ## for 20 century
                return 3
        elif (n==3 or n==14 or n==20 or n==25):     ## for each have same days
            if y==18:                               ## for 18 century
                return 7
            elif y==19:                             ## for 19 century
                return 5
            else:                                   ## for 20 century
                return 4
        elif (n==4 or n==9 or n==15 or n==26):      ## for each have same days
            if y==18:                               ## for 18 century
                return 1
            elif y==19:                             ## for 19 century
                return 6
            else:                                   ## for 20 century
                return 5
        else:                                       ## for each have same days
            if y==18:                               ## for 18 century
                return 2
            elif y==19:                             ## for 19 century
                return 7
            else:                                   ## for 20 century
                return 6
    else:
        print ("Invalid year")
        return -1