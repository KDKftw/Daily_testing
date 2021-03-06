from to_import import acceptConsent2, URL, URL_stat, caps, URL_groupsearch, closeExponeaBanner
from to_import_secret import sendEmail
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


##driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver94.exe")
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver96.exe")
URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?qf=109_0_50|386_1_0|108_1_0&sortby=PriceTotal&sa=2138|1949|2730&tt=1&to=4312&dd=2021-12-01&rd=2021-12-31&nn=7|8|9&ac1=2&m=5"
##URL_SRL = "https://www.eximtours.cz/vysledky-vyhledavani?tt=0&ac1=2&dd=2021-08-27&rd=2021-09-26&nn=7&d=63720|63719&pf=0&pt=900000"

def SRLtestV2(driver):
    x=0         ##variable for taking the first hotel, starting at 0
    windowHandle = 1  ##variable for handling windows, gotta start on 1

    driver.get(URL_SRL)
    wait = WebDriverWait(driver, 150000)

    time.sleep(2)
    acceptConsent2(driver)
    time.sleep(2)
    closeExponeaBanner(driver)

    try:
        hotelyAllKarty = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")

    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem SRL hotelyAllKarty" + url
        sendEmail(msg)

    for WebElement in hotelyAllKarty:

        terminZajezdu = driver.find_elements_by_xpath("//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
        terminZajezduSingle = driver.find_element_by_xpath("//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

        wait.until(EC.visibility_of(terminZajezduSingle))
        ##print(terminZajezdu[x].text)

        linkDetail = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
        linkDetailActualUrl = linkDetail[x].get_attribute("href")
        ##print(linkDetailActualUrl)

        stravaZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
        stravaZajezduString = stravaZajezdu[x].text

        pokojZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
        pokojZajezduString = pokojZajezdu[x].text
        ##print(pokojZajezduString)

        cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
        cenaZajezduAllString = cenaZajezduAll[x].text
        ##print(cenaZajezduAllString)

        cenaZajezduAdult = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
        cenaZajezduAdultString = cenaZajezduAdult[x].text
        print(cenaZajezduAdultString)



        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[windowHandle])
        driver.get(linkDetailActualUrl)

        closeExponeaBanner(driver)

        time.sleep(1)       ##natvrdo aby se to neposralo

        detailTerminSedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
        ##print(detailTerminSedivka.text)

        detailStravaSedivka = driver.find_elements_by_xpath("//*[@class='fshr-detail-summary-paragraph']")
        detailStravaSedivkaString = detailStravaSedivka[1].text         ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully

        detailPokojSedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
        detailPokojSedivkaString = detailPokojSedivka.text
        detailPokojSedivkaString = detailPokojSedivkaString[:-3]            ##need to be edited cuz there is random spaces and "?" in the element
        ##print(detailPokojSedivkaString)

        detailCenaAll = driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
        detailCenaAllString = detailCenaAll.text
        ##print(detailCenaAllString)
        try:
            detailCenaAdult = driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
            detailCenaAdultString = detailCenaAdult.text
            print(detailCenaAdultString)

        except NoSuchElementException:
            pass


        if detailPokojSedivkaString == pokojZajezduString:
            print("pokoje sed?? srl vs detail")
        else:
            print(" nesed?? pokoj SRL vs sedivka")

        if detailStravaSedivkaString == stravaZajezduString:
            print("stravy sed?? srl vs detail")

        else:
            print( "nesed?? strava srl vs ssedika")

        if detailCenaAllString == cenaZajezduAllString:
            print ("ceny all sed?? srl vs detail")

        else:
            print("ceny all problem srl vs detail")

        if detailCenaAdultString == cenaZajezduAdultString:
            print(" cena adult sed?? srl vs detail")

        else:
            print("cena adult nesedi srl vs detail")

        driver.switch_to.window(driver.window_handles[0])   ##this gotta be adjusted based on what test is executed
        ##for daily test needs to be set on 1 so it gets on the SRL

        x = x +1
        print(x)
        windowHandle = windowHandle + 1
        print(windowHandle)

SRLtestV2(driver)