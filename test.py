import datetime

# print(datetime.date())
# print(datetime.date(2001, 1, 2))
# print(datetime.toordinal())
d = str(datetime.datetime.fromordinal(7300))[:-9]
print(str(int(d[:4]) + 2001) + " " + str(int(d[5:7])) + " " + str(int(d[8:])))