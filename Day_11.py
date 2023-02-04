# How many seconds are in a year?
print("==> HOW MANY SECONDS DO WE HAVE IN A YEAR? <==")
print()
sec = float(input("How many seconds do we have in 1 mins: "))
min = float(input("How many mins do we have in 1 hours: "))
hr = float(input("How many hours do we have in a day: "))
yr = float(input("How many days makes a year: "))
#yrs = 366
sum1 = sec * min * hr * yr
sum2 = sec * min * hr * yr
print()
if yr == 365:
    print("Congratulation!! its a whole year",sum1,"Seconds")
else:
    print("Congratulation!! its a leap year in",sum2,"Seconds")
