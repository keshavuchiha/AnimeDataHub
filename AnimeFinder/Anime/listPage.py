
from time import sleep
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Anime.getLinks import Links
from Anime.VideoPage import VideoPage
from Anime.MoreInfo import MoreInfo
class ListPage():
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def startChar(self,char:str):
        char=char[0].upper()
        # self.driver.find_element(By.XPATH,f'//button[text()="{char}"]')
        # sleep(2)
        print(f'//button[text()="{char}"]')
        xpath=f'//button[text()="{char}"]'
        WebDriverWait(self.driver,timeout= 20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="listplace"]/div')))
        print('waited')
        link=self.driver.find_element(By.XPATH,xpath)
        link.click()

        anime=self.driver.find_elements(By.XPATH,'//div[@id="listplace"]/div')
        print(anime[2].text)
        # //div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub"))]
        subAnime=self.driver.find_elements(By.XPATH,'//div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub"))]')
        for anime in subAnime:
            # print(anime.get_attribute('innerHTML'))
            # btn
            if(anime.get_attribute('innerHTML')=='Kimetsu no Yaiba'):
                
                # 
                # self.driver.execute_script('arguments[0].scrollIntoView(true);',anime)
                # WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub")) and text()="Kimetsu no Yaiba"]')))
                
                # btn=self.driver.find_element(By.XPATH,'//div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub")) and text()="Kimetsu no Yaiba"]')
                # self.driver.execute_script('arguments[0].click();',anime)
                # self.driver.get(anime.get_attribute('href'))
                print(anime.get_attribute('href'))
                # anime.click()
                # time.sleep(5)
                btn=anime
                # self.driver.get(anime.get_attribute('href'))
        self.driver.execute_script('arguments[0].scrollIntoView(true);',btn)
        self.driver.execute_script('arguments[0].click();',btn)
        videoPage=VideoPage(self.driver)
        # videoPage.getEpisodeCount()
        videoPage.moreInfo()
        moreInfo=MoreInfo(self.driver)
        # moreInfo.synopsis()
        moreInfo.similarTab()
        


        
