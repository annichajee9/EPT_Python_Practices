m_and_y = list(map(int, input().split()))
updated_year = m_and_y[1] - 543

if m_and_y[0] == 1:
    print("Day=31")
elif m_and_y[0] == 2:
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
elif m_and_y[0] == 3:
    print("Day=31")
elif m_and_y[0] == 4:
    print("Day=30")
elif m_and_y[0] == 5:
    print("Day=31")
elif m_and_y[0] == 6:
    print("Day=30")
elif m_and_y[0] == 7:
    print("Day=31")
elif m_and_y[0] == 8:
    print("Day=31")
elif m_and_y[0] == 9:
    print("Day=30")
elif m_and_y[0] == 10:
    print("Day=31")
elif m_and_y[0] == 11:
    print("Day=30")
elif m_and_y[0] == 12:
    print("Day=31")
else:
    print("Please input valid month from 1 to 12")