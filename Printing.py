## For Printing The Calendar
## m Represents Which Month It is
## start Represent From Which Day Does Month Starts
## Note: start Represents INT Value i.e 1-7 (Sunday-Saturday)

def leap_printing(start,m):
    print("   S   M   T   W   T   F   S \n")
    if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):    ## for month having date upto 31
        date=1                                                      ## for date
        j=1                                                         ## for providing blank spaces if a month does not start with Sunday
        c=1                                                         ## for first line that when does it change to next line
        while start!=j:                                             ## for providing blank spaces
            print("    ",end="")
            c+=1
            j+=1
        while c<8:                                                  ## for first line that when does it change to next line
            print("  ",date,end="")                                 ## printing value of date
            date +=1                                                ## increasing value of date
            c +=1
        print("\n")                                                 ## for next line
        while date<32:                                              ## for remaining dates
            c=1
            while c<8:
                if date<32:
                    if date<10:
                        print("  ",date,end="")
                    else:
                        print(" ",date,end="")
                    date +=1
                else:
                    break
                c+=1
            print("\n")
    elif (m==4 or m==6 or m==9 or m==11):                           ## for month having date upto 31
        date=1                                                      ## for date
        j=1                                                         ## for providing blank spaces if a month does not start with Sunday
        c=1                                                         ## for first line that when does it change to next line
        while start!=j:                                             ## for providing blank spaces
            print("    ",end="")
            c+=1
            j+=1
        while c<8:                                                  ## for first line that when does it change to next line
            print("  ",date,end="")                                 ## printing value of date
            date +=1                                                ## increasing value of date
            c +=1
        print("\n")                                                 ## for next line
        while date<31:                                              ## for remaining dates
            c=1
            while c<8:
                if date<31:
                    if date<10:
                        print("  ",date,end="")
                    else:
                        print(" ",date,end="")
                    date +=1
                else:
                    break
                c+=1
            print("\n")
    else:                                                           ## for feb month
        date=1                                                      ## for date
        j=1                                                         ## for providing blank spaces if a month does not start with Sunday
        c=1                                                         ## for first line that when does it change to next line
        while start!=j:                                             ## for providing blank spaces
            print("    ",end="")
            c+=1
            j+=1
        while c<8:                                                  ## for first line that when does it change to next line
            print("  ",date,end="")                                 ## printing value of date
            date +=1                                                ## increasing value of date
            c +=1
        print("\n")                                                 ## for next line
        while date<30:                                              ## for remaining dates
            c=1
            while c<8:
                if date<30:
                    if date<10:
                        print("  ",date,end="")
                    else:
                        print(" ",date,end="")
                    date +=1
                else:
                    break
                c+=1
            print("\n")

## SIMILAR LOGIC IS FOR NON_LEAP PRINITNG
def non_leap_printing(start,m):
    print("   S   M   T   W   T   F   S")
    if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        date=1
        j=1
        c=1
        while start!=j:
            print("    ",end="")
            c+=1
            j+=1
        while c<8:
            print("  ",date,end="")
            date +=1
            c +=1
        print("\n")
        while date<32:
            c=1
            while c<8:
                if date<32:
                    if date<10:
                        print("  ",date,end="")
                    else:
                        print(" ",date,end="")
                    date +=1
                else:
                    break
                c+=1
            print("\n")
    elif (m==4 or m==6 or m==9 or m==11):
        date=1
        j=1
        c=1
        while start!=j:
            print("    ",end="")
            c+=1
            j+=1
        while c<8:
            print("  ",date,end="")
            date +=1
            c +=1
        print("\n")
        while date<31:
            c=1
            while c<8:
                if date<31:
                    if date<10:
                        print("  ",date,end="")
                    else:
                        print(" ",date,end="")
                    date +=1
                else:
                    break
                c+=1
            print("\n")
    else:
        date=1
        j=1
        c=1
        while start!=j:
            print("    ",end="")
            c+=1
            j+=1
        while c<8:
            print("  ",date,end="")
            date +=1
            c +=1
        print("\n")
        while date<29:
            c=1
            while c<8:
                if date<29:
                    if date<10:
                        print("  ",date,end="")
                    else:
                        print(" ",date,end="")
                    date +=1
                else:
                    break
                c+=1
            print("\n")