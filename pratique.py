from bs4 import BeautifulSoup
from selenium import webdriver
import time

noReg = "1234567"   # Numéro de personne
dob = "01.01.2000"  # Date de naissance JJ.MM.AAAA

mois_voulu = 6 # 1-12
jour_min = 21  # 1-31
jour_max = 27  # 1-31

driver = webdriver.Chrome()
driver.get("https://ge.ch/cari-online/examensPublic")

while True: #yolo
  if driver.find_elements_by_name("login"):
    print("Logging in... ", end='')
    driver.find_element_by_css_selector("input[name='noReg']").send_keys(noReg)
    driver.find_element_by_css_selector("input[name='dateJJ']").send_keys(dob.split('.')[0])
    driver.find_element_by_css_selector("input[name='dateMM']").send_keys(dob.split('.')[1])
    driver.find_element_by_css_selector("input[name='dateAAAA']").send_keys(dob.split('.')[2])
    driver.find_element_by_css_selector("input[name='valider']").click()
    time.sleep(1)
    print("Done")

  if driver.find_elements_by_name("selectExamens"):
    print("Voir dates... ", end='')
    driver.find_element_by_xpath("//*[contains(text(), 'Déplacer')]").click()
    time.sleep(1)
    print("Done")

  if driver.find_elements_by_id("idDivTablePlaceLibre"):
    print("Check dates libres... ", end='')
    while driver.find_elements_by_css_selector("input[name='prevWeek']"): # Ramener à la premiere semaine dispo
      driver.find_element_by_css_selector("input[name='prevWeek']").click()

    i = 0
    dates_libres = []
    chercher = True

    while i <=5:
      l = driver.find_elements_by_xpath("//a[contains(@onmouseover, 'window.status')]")
      for el in l:
        dates_libres.append(el.get_attribute('onmouseover').split("'")[1])
        if int(dates_libres[-1].split('.')[1]) == mois_voulu and int(dates_libres[-1].split('.')[0]) >= jour_min and int(dates_libres[-1].split('.')[0]) <= jour_max:
          el.click()
          time.sleep(1)
          driver.find_element_by_css_selector("input[name='confirm']").click()
          print("\n ALERTE : Date changée pour",dates_libres[-1])
          chercher = False
          break
        i+=1
      
      if chercher:
        driver.find_element_by_css_selector("input[name='nextWeek']").click()
      else:
        break

    dates_libres = dates_libres[:5]
    time.sleep(1)
    print("Done")
    print(dates_libres)
    
    if chercher == False:
      break
  time.sleep(10)  # Intervalle de pause