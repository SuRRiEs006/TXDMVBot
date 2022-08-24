import DMVSlotFinder
import threading


outcome = False
retryCount = 0

while True:

    testProfile = DMVSlotFinder.BookingProfile("surna","satpalli","12/2002","11","734","08/2002")
    outcome = testProfile.main()
    print(outcome)
    if (outcome == None) & (retryCount<3):
        retryCount += 1
    elif (outcome == None):
        break
    elif (outcome == True):
        break
    
    
    
    
    #testProfile = DMVSlotFinder.BookingProfile("profilef","profilel","11/11/2001","1111","75034","10/03/2002")
    #testProfile = DMVSlotFinder.BookingProfile("namef","namel","11/12/2001","1111","75034","10/03/2002")