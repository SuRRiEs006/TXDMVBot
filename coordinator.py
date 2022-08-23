import DMVSlotFinder
import threading

testProfile = DMVSlotFinder.BookingProfile("surya venkata sai vamsi krishna","sathanapalli","12/11/2002","1111","75034","08/23/2002")
outcome = testProfile.main()



while True:
    #testProfile = DMVSlotFinder.BookingProfile("profilef","profilel","11/11/2001","1111","75034","10/03/2002")
    testProfile = DMVSlotFinder.BookingProfile("surya venkata sai vamsi krishna","sathanapalli","12/11/2002","1111","75034","08/23/2002")
    #threading.Thread(target=DMVSlotFinder.BookingProfile, args=("profilef","profilel","11/11/2001","1111","75034","10/03/2002"))
    outcome = testProfile.main()
    print(outcome)
    
    
    
    
    #testProfile = DMVSlotFinder.BookingProfile("profilef","profilel","11/11/2001","1111","75034","10/03/2002")
    #testProfile = DMVSlotFinder.BookingProfile("namef","namel","11/12/2001","1111","75034","10/03/2002")