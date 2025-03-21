year = int(input())
updated_year = year - 543
if updated_year % 4 == 0:
        if updated_year % 100 == 0:
            if updated_year % 400 == 0:
                print("Day=29")
            else:
                print("Day=28")
        else:
            print("Day=29") 
else:
    print("Day=28")