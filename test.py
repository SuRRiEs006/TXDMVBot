import time
earliestBooked = "8/18/2022 1:00 PM".split(" ")[0]
newBooked = "8/17/2022"

formattedBooked = time.strptime("10/03/2022", "%m/%d/%Y")
formattedEarliest = time.strptime("10/03/2002", "%m/%d/%Y")
formattedNew = time.strptime("08/18/2022", "%m/%d/%Y")

if (formattedBooked > formattedNew) and (formattedNew >= formattedEarliest):
    print("GETTING BOOKED!")