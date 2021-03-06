import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, caps, closeExponeaBanner
from selenium.common.exceptions import NoSuchElementException
import requests
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")

URL_detail_exim = "https://www.fischer.cz/recko/kreta-heraklion/bali/athina?DS=1024&GIATA=8225&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=9043&MT=2&RT=22&NN=7&RD=2022-07-14&DD=2022-07-07&DP=2682&MNN=7|8|9&TT=1&PID=5613&DPR=EXIM%20TOURS&TTM=1&DF=2022-07-07|2022-08-07&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
URL_dx = "https://www.fischer.cz/hotely/recko/kreta/sissi/bella-vista-sissi-recko?DS=2&GIATA=1020&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=282531&MT=0&RT=22&NN=7&RD=2022-07-08&DD=2022-07-01&DP=2563&MNN=7|8|9&TT=1&PID=AMTSGR2CHQ&DPR=OTSCKF&TTM=1&DF=2022-07-01|2022-08-01&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
URL_statik = "https://www.fischer.cz/recko/samos/pythagorion/maritsa-bay?DS=1&GIATA=17012&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=65254&MT=2&DI=47&RT=15&NN=7&RD=2022-08-30&DD=2022-08-23&DP=4312&MNN=7|8|9&TT=1&PID=SMMAR&DPR=Fischer&TTM=1&DF=2022-08-23|2022-09-23&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
wait = WebDriverWait(driver, 150000)


def omlouvamese_paragraph(driver):
    time.sleep(1)
    try:
        omlouvameParagraph = driver.find_element_by_xpath("//*[@class='fshr-paragraph fshr-paragraph--centered']")
        if omlouvameParagraph.is_displayed():
            return

    except NoSuchElementException:
        pass

def detail_fotka(driver):
    imageDetail = driver.find_element_by_xpath("//*[@id='gallery01Trigger']//img")
    imageDetailSrc = imageDetail.get_attribute("src")
    try:
        driver.set_page_load_timeout(5)
        driver.get(imageDetailSrc)
    except TimeoutException:
        url = driver.current_url
        msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
        sendEmail(msg)

    try:
        image = driver.find_element_by_xpath("/html/body/img")
        if image.is_displayed():
            print("its ok")
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
        sendEmail(msg)


def detail_terminy_filtr_meal(driver):
    try:
            terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
            wait.until(EC.visibility_of(terminyCeny))
            ##terminyCeny.click()
            driver.execute_script("arguments[0].click();", terminyCeny)
            try:
                potvrdit = driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")

                driver.execute_script("arguments[0].click();", potvrdit)

            except NoSuchElementException:
                url = driver.current_url
                msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
                sendEmail(msg)


    except NoSuchElementException:
            url = driver.current_url
            msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
            sendEmail(msg)


    try:
        stravovaniBox = driver.find_element_by_xpath("//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']")
        wait.until(EC.visibility_of(stravovaniBox))
        driver.execute_script("arguments[0].click();", stravovaniBox)
        try:
            #allInclusiveBox = driver.find_element_by_xpath("//*[contains(text(), 'All inclusive')]")
            #wait.until(EC.visibility_of(allInclusiveBox))
            ##allInclusiveBox.click()
            stravyBox = driver.find_elements_by_xpath("//*[@name='detailFilterCatering']")


            driver.execute_script("arguments[0].click();", stravyBox[1])


            try:
                ##potvrditButtonBox = driver.find_element_by_xpath("//*[@class='fshr-filter-footer'] //*[contains(text(), 'Potvrdit')]")

                #potvrditButtonBox.click()
                driver.execute_script("arguments[0].click();", stravovaniBox)       ##workaround, klikni na box to confirm the choice

            except NoSuchElementException:
                url = driver.current_url
                msg = "stravaBox, potvrzeni stravy na detailu hotelu probl??m, NoSuchElementException " + url
                sendEmail(msg)

        except NoSuchElementException:
            url = driver.current_url
            msg = "allInclusiveBox, zvolen?? stravy na detailu hotelu probl??m, NoSuchElementException " + url
            sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "stravovaniBox, otev??en?? filtru stravov??n?? detail hotelu, NoSuchElementException " + url
        sendEmail(msg)

    omlouvamese_paragraph(driver)

    zvolenaStravaVboxu = driver.find_element_by_xpath("//*[@class='js-subvalue f_text--highlighted']")
    zvolenaStravaVboxuString = zvolenaStravaVboxu.text

    ##print(zvolenaStravaVboxuString)

    stravaVterminech = driver.find_elements_by_xpath("//*[@class='fshr-termin-catering js-tooltip js-tooltip--onlyDesktop']")
    stravaVterminechString = []


   ##ty for loopy se nezapnou pokud pocet vysledku bude 0
    ##takze treba exim a dx bude casto takto jelikoz se tam nabizi vsechny stravy, ne jen ty available
    x=0
    for _ in stravaVterminech:
        stringos = stravaVterminech[x].text
        stravaVterminechString.append(stringos)
        x=x+1

    time.sleep(1)###eroror element is not attached ? tak chvilku cekacka mozna to solvne

    y=0
    for _ in stravaVterminechString:
        if stravaVterminechString[y] == zvolenaStravaVboxuString:
            ##print("ok")
            ##print(y)
            y=y+1
        else:
            url = driver.current_url
            msg = "na detailu jsem vyfiltroval stravu " + zvolenaStravaVboxuString +"ale pry to nesedi ????k?? python" + url
            sendEmail(msg)
            y=y+1

    ##print(stravaVterminech)
    ##print(stravaVterminechString)

def detail_terminy_filtr_airport(driver):

    try:
                terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
                wait.until(EC.visibility_of(terminyCeny))
                ##terminyCeny.click()
                driver.execute_script("arguments[0].click();", terminyCeny)
                time.sleep(0.5)
                try:
                    potvrdit = driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")
                    ##wait.until(EC.visibility_of(potvrdit))
                    driver.execute_script("arguments[0].click();", potvrdit)

                except NoSuchElementException:
                    url = driver.current_url
                    msg = "Problem prepnuti na terminy a ceny na detailu hotelu,potvrdit,  NoSuchElementException " + url
                    sendEmail(msg)

    except NoSuchElementException:
                url = driver.current_url
                msg = "Problem prepnuti na terminy a ceny na detailu hotelu, NoSuchElementException " + url
                sendEmail(msg)

    try:
            dopravaBox = driver.find_element_by_xpath("//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']")
            wait.until(EC.visibility_of(dopravaBox))
            driver.execute_script("arguments[0].click();", dopravaBox)
            try:
                dopravaBrno = driver.find_element_by_xpath("//*[@data-value='4305']")       ##natvrdo brno, no list shenanigans
                driver.execute_script("arguments[0].click();", dopravaBrno)

                time.sleep(0.5)
                try:
                    ##potvrditButtonBox = driver.find_element_by_xpath("//*[@class='fshr-filter-footer'] //*[contains(text(), 'Potvrdit')]")
                    ##potvrditButtonBox = driver.find_element_by_xpath("//*[@class='fshr-button fshr-button--commonImportance fshr-button--big js-filterClose']")
                    ##potvrditButtonBox = driver.find_element_by_xpath("//*[@class='js-filter js-filter--detail fshr-filter fshr-filter--travel js-change-detection fshr-filter--active']//*[@class='fshr-filter-wrapper js-filter-window']//*[@class='fshr-filter-footer']//*[@class='fshr-button fshr-button--commonImportance fshr-button--big js-filterClose']")
                    ##wait.until(EC.visibility_of(potvrditButtonBox))
                    #potvrditButtonBox.click()
                    driver.execute_script("arguments[0].click();", dopravaBox) ##workaround, proste klikne znova na doprava box aby se to propsalo, potvrdit button mi nejak blbnul
                    ##driver.execute_script("arguments[0].click();", potvrditButtonBox)

                except NoSuchElementException:
                    url = driver.current_url
                    msg = "potvrditButtonBox, potvrzeni dopravy na detailu hotelu probl??m, NoSuchElementException " + url
                    sendEmail(msg)

            except NoSuchElementException:
                url = driver.current_url
                msg = "dopravaBrno, zvolen?? dopravy na detailu hotelu probl??m, NoSuchElementException " + url
                sendEmail(msg)

    except NoSuchElementException:
            url = driver.current_url
            msg = "dopravaBox, zvolen?? dopravy na detailu hotelu probl??m, NoSuchElementException " + url
            sendEmail(msg)

    time.sleep(1)       ##cekacka na terminy load
    omlouvamese_paragraph(driver)

    try:
        pocetZobrazenychTerminu = driver.find_elements_by_xpath("//*[@class='fshr-termins-table-item-header js-toggleSlide']")      ##locator jen na pocet odletu alokuje vic veci nez je actual terminu tak pro
                                                                                                                                    ##for loop pouziju tohle = 20
    except NoSuchElementException:
        url = driver.current_url
        msg = "pocetZobrazenychTerminu, filtrovani dle letu detail hotelu, mozna jen nema odlety na X, NoSuchElementException " + url
        sendEmail(msg)


    try:
        odletyTerminy = driver.find_elements_by_xpath("//*[@class='fshr-termin-departure-from']") ##prvni locator je "odlet" takze zacnu na pozici jedna, vyloopuje se to podle poctu terminu, should be ok
    except NoSuchElementException:
            url = driver.current_url
            msg = "odletyTerminy, nejsou odlety na brno, most likely not a bad thing, NoSuchElementException " + url
            sendEmail(msg)
    y=1
    for _ in pocetZobrazenychTerminu:
            if odletyTerminy[y].text == "Brno":         ##tady je nutny pricitat +2 protoze je tam 41 results (s tim ze jeden je "odlet"), kazdy sudy cislo je mezera/blank space for some reason
                ##print(odletyTerminy[y].text)
                y=y+2
            else:
                url = driver.current_url
                ##print(odletyTerminy[y].text)
                msg = "na detailu jsem vyfiltroval odlet na brno ale pry to nesedi ????k?? python " + url
                sendEmail(msg)
                y=y+2

def detail_map_check(driver):
    driver.get(URL_statik)
    time.sleep(5)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)


    time.sleep(7)  ##try except na kolecko, pokud ok tak click, nenajde tak pokracovat dal
    #koleckoCislo = driver.find_element_by_xpath(
       # "//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
    #wait.until(EC.element_to_be_clickable(koleckoCislo))
    #koleckoCislo.click()

    try:
        actualHotelPin = driver.find_element_by_xpath(
            "//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
        ##actualHotelPin.click()
        driver.execute_script("arguments[0].click();", actualHotelPin)
        print("SUCCESS detail_map_check")
    except NoSuchElementException:
        url = driver.current_url
        msg = "Nenasli se mapa v /stat " + url
        print("FAIL detail_map_check")
#detail_terminy_filtr_airport(driver)
#driver.get(URL_detail_exim)
#detail_terminy_filtr_meal(driver)
#driver.get(URL_detail_exim)
#detail_fotka(driver)

detail_map_check(driver)