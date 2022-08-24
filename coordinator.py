import DMVSlotFinder
import threading


outcome = False


while outcome != True & outcome == None:

    testProfile = DMVSlotFinder.BookingProfile("surna","satpalli","12/2002","11","734","08/2002")
    outcome = testProfile.main()
    print(outcome)

    
    
    
    
    #testProfile = DMVSlotFinder.BookingProfile("profilef","profilel","11/11/2001","1111","75034","10/03/2002")
    #testProfile = DMVSlotFinder.BookingProfile("namef","namel","11/12/2001","1111","75034","10/03/2002")