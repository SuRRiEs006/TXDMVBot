from selenium import webdriver
import time
import random



class BookingProfile:

    def __init__(self,applicantFirstName,applicantLastName,DOB,lastFourSSN,postCode):
        self.applicantFirstName = applicantFirstName
        self.applicantLastName = applicantLastName
        self.DOB = DOB
        self.lastFourSSN = lastFourSSN
        self.postCode = postCode
        self.dateBooked = None
        self.browser = None


    def bookAvalible(self,index):
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[2]/div/table/tbody/tr["+str(index)+"]/td[4]/i").click()
        time.sleep(7)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[1]/div").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[2]/table/tbody/tr/td[2]/div/div/div").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[4]/div/div[2]/button").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[4]/div/div[2]/button").click()

    def enterText(self,xpath,text):
        self.browser.find_element_by_xpath(xpath).click()
        self.browser.find_element_by_xpath(xpath).send_keys(text)

    def earlierDateFound(self,newDate,index):
        formattedBooked = time.strptime(self.dateBooked, "%m/%d/%Y")

        formattedNew = time.strptime(newDate, "%m/%d/%Y")
        earlierDateFoundResult = formattedBooked > formattedNew
        if earlierDateFoundResult == True:
            print("FOUNDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            self.bookAvalible(index)
        return(earlierDateFoundResult)

    def main(self):
        browser = webdriver.Chrome("chromedriver.exe")
        self.browser = browser
        browser.get("https://public.txdpsscheduler.com/")
        time.sleep(4)
        browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/button[1]").click()
        time.sleep(4)

        self.enterText("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[2]/div/div[1]/div/input",self.applicantFirstName)
        time.sleep(0.5)

        self.enterText("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[3]/div/div[1]/div/input",self.applicantLastName)
        time.sleep(0.5)

        self.enterText("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[4]/div/div[1]/div/input",self.DOB)
        time.sleep(0.5)

        self.enterText("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[3]/div[5]/div/div[1]/div/input",self.lastFourSSN)
        time.sleep(0.5)


        browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/form/div[2]/div[4]/button").click()

        time.sleep(10)
        browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/div[5]/div/button").click()





        time.sleep(3)

        self.dateBooked = (browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/div[4]/div[2]").text).split(" ")[0]

        print(self.dateBooked)

        browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/section/div/main/div/section/div[2]/div/div/div[5]/div[2]/div[2]/button").click()

        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/button").click()


        time.sleep(3)

        browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div[1]/input").click()
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div[1]/input").send_keys(self.postCode)

        earlierFoundBooked = False
        while (earlierFoundBooked != True):
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/form/div/div[2]/div[2]/div/div[2]/button").click()
            time.sleep(10)

            index = 1
            while (earlierFoundBooked != True) and (index <= 4):
                dateAvalible = browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[2]/div/table/tbody/tr["+str(index)+"]/td[3]").text
                print(self.earlierDateFound(dateAvalible,index))
                index += 1
            time.sleep(random.randint(30,60))
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[5]/div/div[1]/button").click()
            time.sleep(5)


        print("DONE")
        time.sleep(100)

testProfile = BookingProfile("firstF","firstL","11/11/2001","1111","75034")
testProfile.main()
applicantFirstName = "firstF"
applicantLastName = "firstL"
DOB = "11/11/2001"
lastFourSSN = "1111"
postCode = "75034"