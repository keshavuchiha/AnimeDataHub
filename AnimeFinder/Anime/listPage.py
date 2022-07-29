
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Anime.getLinks import Links
class ListPage():
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def startChar(self,char:str):
        char=char[0].upper()
        # self.driver.find_element(By.XPATH,f'//button[text()="{char}"]')
        # sleep(2)
        print(f'//button[text()="{char}"]')
        xpath=f'//button[text()="{char}"]'
        WebDriverWait(self.driver,timeout= 15).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="listplace"]/div')))
        print('waited')
        link=self.driver.find_element(By.XPATH,xpath)
        link.click()

        anime=self.driver.find_elements(By.XPATH,'//div[@id="listplace"]/div')
        print(anime[2].text)
        # //div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub"))]
        subAnime=self.driver.find_elements(By.XPATH,'//div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub"))]')
        for anime in subAnime:
            print(anime.get_attribute('innerHTML'))
            if(anime.get_attribute('innerHTML')=='Kimetsu no Yaiba'):
                anime.click()
        


        
