import time
dateBooked = "12/9/2022 1:00 PM".split(" ")[0]
newBooked = "12/11/2002"


formattedBooked = time.strptime(dateBooked, "%m/%d/%Y")

formattedNew = time.strptime(newBooked, "%m/%d/%Y")
print(formattedBooked > formattedNew)