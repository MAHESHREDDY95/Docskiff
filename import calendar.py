import calendar

def date_inter():
    x = input("Enter: YYYMMDD FORMATE:")
    x1 ="20250927"
    yr = int(x[0:4])
    mn = int(x[4:6])
    yr1 = int(x1[0:4])
    mn1 = int(x1[4:6])
    da = int(x[6:])

    for month in range(mn, 10):
        mycal = calendar.monthcalendar(yr, month)
        week1 = mycal[0]
        week2 = mycal[1]
        week3 = mycal[2]
        week4 = mycal[3]

        if week1[calendar.SATURDAY] != 0:
            inter_d1 = week1[calendar.SATURDAY]
            w1 = int("%d%s%s" % (yr,month,inter_d1))
            if w1 % 5 == 0:
                if len(str(month)) == 1 and len(str(inter_d1)) == 1:
                    month = "0" + str(month)
                    inter_d1 = "0" + str(inter_d1)
                    print(int("%d%s%s" % (yr,month,inter_d1)))
                else:
                    print(int("%d%s%s" % (yr,month,inter_d1)))
    
        if week2[calendar.SATURDAY] != 0:
            inter_d2 = week2[calendar.SATURDAY]
            w2 = int("%d%s%s" % (yr,month,inter_d2))
            if w2 % 5 == 0:
                if len(str(month)) == 1 and len(str(inter_d2)) == 1:
                    month = "0" + str(month)
                    inter_d2 = "0" + str(inter_d2)
                    print(int("%d%s%s" % (yr,month,inter_d2)))
                else:
                    print(int("%d%s%s" % (yr,month,inter_d2)))

        if week3[calendar.SATURDAY] != 0:
            inter_d3 = week3[calendar.SATURDAY]
            w3 = int("%d%s%s" % (yr,month,inter_d3))
            if w3 % 5 == 0:
                if len(str(month)) == 1:
                    month = "0" + str(month)
                    print(int("%d%s%s" % (yr,month,inter_d3)))
                else:
                    print(int("%d%s%s" % (yr,month,inter_d3)))

        if week4[calendar.SATURDAY] != 0:
            inter_d4 = week4[calendar.SATURDAY]
            w4 = int("%d%s%s" % (yr,month,inter_d4))
            if w4 % 5 != 0:
                if len(str(month)) == 1:
                    month = "0" + str(month)
                if len(str(inter_d4)) == 1:
                    inter_d4 = "0" + str(inter_d4)
                    print(int("%d%s%s" % (yr,month,inter_d4)))
                else:
                  print(int("%d%s%s" % (yr,month,inter_d4)))


date_inter() 
