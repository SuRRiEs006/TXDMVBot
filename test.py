import time
earliestBooked = "8/18/2022 1:00 PM".split(" ")[0]
newBooked = "8/17/2022"


formattedBooked = time.strptime(earliestBooked, "%m/%d/%Y")
formattedNew = time.strptime(newBooked, "%m/%d/%Y")


print(formattedNew >= formattedBooked)