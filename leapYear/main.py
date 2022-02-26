year = input("year name")

year = int (year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes")
        else:
            print("NO")
    else:
        print("yes")
else:
    print("NO")