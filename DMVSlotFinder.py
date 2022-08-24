from selenium import webdriver
from datetime import datetime
import time
import random



class BookingProfile:

    def __init__(self,applicantFirstName,applicantLastName,DOB,lastFourSSN,postCode,idealDate):
        self.noNeedToRun = False
        self.applicantFirstName = applicantFirstName
        self.applicantLastName = applicantLastName
        self.DOB = DOB
        self.lastFourSSN = lastFourSSN
        self.postCode = postCode
        self.idealDate = idealDate #MM/DD/YEAR
        self.dateBooked = None
        self.browser = None
        


    def bookAvalible(self,index):
        if index != 0:
            self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[2]/div/table/tbody/tr["+str(index)+"]/td[4]/i").click()
            time.sleep(4)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div[1]/div").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[2]/table/tbody/tr/td[2]/div/div/div").click()
        time.sleep(4)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[4]/div/div[2]/button").click()
        time.sleep(6)
        self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[4]/div/div[2]/button").click()

    def enterText(self,xpath,text):
        self.browser.find_element_by_xpath(xpath).click()
        self.browser.find_element_by_xpath(xpath).send_keys(text)

    def isEarlierDateFound(self,newDate,index):
        formattedBooked = time.strptime(self.dateBooked, "%m/%d/%Y")
        formattedEarliest = time.strptime(self.idealDate, "%m/%d/%Y")
        formattedNew = time.strptime(newDate, "%m/%d/%Y")

        if (formattedBooked > formattedNew) and (formattedNew >= formattedEarliest):
            print("FOUNDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            self.bookAvalible(index)
            if dateBooked == self.idealDate:
                self.noNeedToRun = True
            else:
                self.noNeedToRun = False


    def main(self):
        try:
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
                time.sleep(11)

                index = 1
                dateAvalible = browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[1]/div/table/tbody/tr/td[3]").text
                earlierFoundBooked = self.isEarlierDateFound(dateAvalible,0)
                while (earlierFoundBooked != True) and (index <= 4):
                    dateAvalible = browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[2]/div/table/tbody/tr["+str(index)+"]/td[3]").text
                    earlierFoundBooked = self.isEarlierDateFound(dateAvalible,index)
                    index += 1
                time.sleep(random.randint(30,60))
                if earlierFoundBooked != True :
                    browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div/div/section/div/main/div/section/div[2]/div/div[5]/div/div[1]/button").click()
                else:
                    return(self.noNeedToRun)
        except:
            self.browser.save_screenshot(self.applicantFirstName + str(datetime.now().strftime("     %d-%m-%Y-%H-%M-%S")) + ".png")
            return(False)

